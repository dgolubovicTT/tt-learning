#!/usr/bin/env python3
"""
2-D weight fracturing on an (8, 4) Galaxy, for W_qkv.

Mesh is opened as (8, 4)  -- conftest.py:18
  mesh axis 0 : 8 chips  <- N (qkv width / heads)      index a
  mesh axis 1 : 4 chips  <- K (model dim H)            index b

  weight     dims=(3, 2)   axis0 <- tensor dim 3 (N), axis1 <- tensor dim 2 (K)
  activation dims=(None,-1) axis0 replicate,          axis1 <- tensor dim -1 (H = K)
  reduction  cluster_axis=1  (the 4 chips that share an N block)

Emits galaxy-2d.svg.frag (page) and galaxy-2d.excalidraw (editable).
"""
import json

NA, NB = 8, 4                      # chips on axis 0, axis 1
CELL = 34
W_X, W_Y = 246, 78                 # weight grid origin
X_X, X_Y = 40, 256                 # activation grid origin
Y_Y = 256                          # output row shares the activation's y
HL_A, HL_B = 2, 1                  # the highlighted chip (a, b)
MESH_X, MESH_Y = 610, 78

def esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def t(x, y, s, size=10, fill="currentColor", anchor="start", w=None, rot=None):
    a = f' font-weight="{w}"' if w else ""
    r = f' transform="rotate({rot} {x} {y})"' if rot else ""
    return (f'<text x="{x}" y="{y}" font-family="ui-monospace, monospace" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}"{a}{r}>{esc(s)}</text>')

def svg():
    o, W, H = [], 880, 470
    o.append(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{esc(ARIA)}">')
    o.append('<defs><marker id="g2a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
             'orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker>'
             '<marker id="g2r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
             'orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="var(--ccl)"/></marker></defs>')

    # ---------------- weight W [K, N] : 4 rows (K) x 8 cols (N) ----------------
    o.append(t(W_X, 34, "WEIGHT   W_qkv  [K, N]", 11, "var(--ink)", w="600"))
    o.append(t(W_X, 50, "N = qkv width, cut 8 ways  →  mesh axis 0", 9.5, "var(--local)"))
    o.append(t(W_X, 62, "K = H,         cut 4 ways  →  mesh axis 1", 9.5, "var(--ccl)"))
    for b in range(NB):
        for a in range(NA):
            x, y = W_X + a*CELL, W_Y + b*CELL
            hit = (a == HL_A and b == HL_B)
            fill = "var(--ccl-wash)" if hit else "var(--surface-2)"
            o.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" fill="{fill}" '
                     f'stroke="var(--rule)" stroke-width="1"/>')
            if hit:
                o.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" fill="none" '
                         f'stroke="var(--ccl)" stroke-width="2.5"/>')
    o.append(f'<line x1="{W_X}" y1="{W_Y-8}" x2="{W_X+NA*CELL}" y2="{W_Y-8}" stroke="var(--local)" '
             f'stroke-width="1.2" marker-end="url(#g2a)"/>')
    o.append(t(W_X+NA*CELL+6, W_Y+NB*CELL+14, "N / 8 per chip", 9, "var(--local)"))
    o.append(t(W_X-10, W_Y+NB*CELL/2, "K / 4", 9.5, "var(--ccl)", "middle", rot=-90))

    # ---------------- activation X [S, K] : 4 col-slices (K) ----------------
    o.append(t(X_X, 232, "ACTIVATION   X  [S, K]", 11, "var(--ink)", w="600"))
    o.append(t(X_X, 248, "the SAME K cut, 4 ways → mesh axis 1", 9.5, "var(--ccl)"))
    for b in range(NB):
        x = X_X + b*CELL
        hit = (b == HL_B)
        fill = "var(--ccl-wash)" if hit else "var(--surface-2)"
        o.append(f'<rect x="{x}" y="{X_Y}" width="{CELL}" height="96" fill="{fill}" '
                 f'stroke="var(--rule)" stroke-width="1"/>')
        if hit:
            o.append(f'<rect x="{x}" y="{X_Y}" width="{CELL}" height="96" fill="none" '
                     f'stroke="var(--ccl)" stroke-width="2.5"/>')
        o.append(t(x+CELL/2, X_Y+96+13, f"b={b}", 9, "var(--ccl)" if hit else "var(--muted)", "middle"))
    o.append(t(X_X, X_Y+124, "K / 4 per chip · replicated across all 8 chips of axis 0", 9, "var(--muted)"))
    o.append(t(X_X-8, X_Y+48, "S", 9.5, "currentColor", "middle"))

    # the correspondence: X slice b  <->  W row b
    o.append(f'<path d="M {X_X+HL_B*CELL+CELL/2} {X_Y-4} L {X_X+HL_B*CELL+CELL/2} {W_Y+NB*CELL+22} '
             f'L {W_X-22} {W_Y+NB*CELL+22} L {W_X-22} {W_Y+HL_B*CELL+CELL/2} L {W_X-4} {W_Y+HL_B*CELL+CELL/2}" '
             f'stroke="var(--ccl)" stroke-width="1.5" fill="none" stroke-dasharray="4 3" marker-end="url(#g2r)"/>')
    o.append(t(X_X+150, W_Y+NB*CELL+18, "slice b of X meets row b of W", 9, "var(--ccl)"))

    # ---------------- the mesh, same shape as the weight grid ----------------
    o.append(t(MESH_X, 34, "THE MESH  (8, 4)", 11, "var(--ink)", w="600"))
    o.append(t(MESH_X, 50, "same grid — chip (a,b) holds block (a,b)", 9.5, "var(--muted)"))
    mc = 22
    for b in range(NB):
        for a in range(NA):
            x, y = MESH_X + a*mc, MESH_Y + b*mc
            hit = (a == HL_A and b == HL_B)
            o.append(f'<rect x="{x}" y="{y}" width="{mc}" height="{mc}" '
                     f'fill="{"var(--ccl-wash)" if hit else "var(--surface)"}" '
                     f'stroke="{"var(--ccl)" if hit else "var(--rule)"}" stroke-width="{2 if hit else 1}"/>')
    o.append(t(MESH_X, MESH_Y+NB*mc+16, "a → axis 0, 8 chips", 9, "var(--local)"))
    o.append(t(MESH_X, MESH_Y+NB*mc+28, "b ↓ axis 1, 4 chips", 9, "var(--ccl)"))
    # reduction runs down a column of the mesh
    rx = MESH_X + HL_A*mc + mc/2
    o.append(f'<line x1="{rx}" y1="{MESH_Y-6}" x2="{rx}" y2="{MESH_Y+NB*mc+4}" stroke="var(--ccl)" '
             f'stroke-width="2" marker-end="url(#g2r)"/>')
    o.append(t(MESH_X+NA*mc+10, MESH_Y+NB*mc/2, "all_reduce", 9.5, "var(--ccl)", w="600"))
    o.append(t(MESH_X+NA*mc+10, MESH_Y+NB*mc/2+13, "cluster_axis=1", 9.5, "var(--ccl)"))
    o.append(t(MESH_X+NA*mc+10, MESH_Y+NB*mc/2+26, "4 chips only", 9, "var(--muted)"))

    # ---------------- what one chip computes ----------------
    by = 408
    o.append(f'<line x1="40" y1="{by-24}" x2="840" y2="{by-24}" stroke="var(--rule)" stroke-width="1"/>')
    o.append(t(40, by-6, "chip (a=2, b=1) computes", 10.5, "var(--ink)", w="600"))
    o.append(t(40, by+12, "X[:, b·K/4 : (b+1)·K/4]   ×   W[b·K/4 : … ,  a·N/8 : …]   =   partial Y  [S, N/8]", 11, "var(--ink)"))
    o.append(t(40, by+30, "[S, K/4]                         [K/4, N/8]                    full N/8 width, only this chip’s quarter of the sum", 9, "var(--muted)"))
    o.append(t(40, by+50, "→ all_reduce over the 4 chips sharing a=2 completes the sum. Output stays cut 8 ways on axis 0.", 10, "var(--ccl)"))
    o.append("</svg>")
    return "\n          ".join(o)

ARIA = ("Two-D weight fracturing on an eight by four Galaxy. The weight W_qkv of shape K by N is drawn as a grid of "
        "four rows by eight columns: N is cut eight ways along mesh axis 0 and K is cut four ways along mesh axis 1. "
        "The activation X of shape S by K is cut along K in exactly the same four places, and each slice is replicated "
        "across all eight chips of axis 0. Slice b of the activation meets row b of the weight. The mesh itself has "
        "the same eight by four shape, so chip a,b simply holds block a,b. One chip multiplies an S by K over four "
        "activation slice with a K over four by N over eight weight block, giving a full-width but partial output, "
        "and an all_reduce down the four chips of a mesh column completes the sum.")

# --------------------------------------------------------------- excalidraw --
_n=[0]
def _id():
    _n[0]+=1; return f"g{_n[0]:04d}"
def _b(tp,x,y,w,h,stroke="#1e1e1e",bg="transparent",**kw):
    e=dict(id=_id(),type=tp,x=x,y=y,width=w,height=h,angle=0,strokeColor=stroke,backgroundColor=bg,
           fillStyle="solid",strokeWidth=1,strokeStyle="solid",roughness=1,opacity=100,groupIds=[],
           frameId=None,roundness=None,seed=_n[0]*7919,version=1,versionNonce=_n[0]*104729,
           isDeleted=False,boundElements=None,updated=1,link=None,locked=False)
    e.update(kw); return e
def er(x,y,w,h,stroke,bg,sw=1): return _b("rectangle",x,y,w,h,stroke,bg,strokeWidth=sw)
def et(x,y,s,size=12,stroke="#1e1e1e"):
    return _b("text",x,y,max(len(l) for l in s.split("\n"))*size*0.6,len(s.split("\n"))*size*1.25,
              stroke,text=s,fontSize=size,fontFamily=3,textAlign="left",verticalAlign="top",
              containerId=None,originalText=s,lineHeight=1.25)
def el(x1,y1,x2,y2,stroke="#1e1e1e",sw=1,arrow=True):
    return _b("arrow" if arrow else "line",x1,y1,abs(x2-x1),abs(y2-y1),stroke,strokeWidth=sw,
              points=[[0,0],[x2-x1,y2-y1]],lastCommittedPoint=None,startBinding=None,endBinding=None,
              startArrowhead=None,endArrowhead="arrow" if arrow else None)

def excalidraw():
    _n[0]=0; e=[]
    e.append(et(W_X,20,"2-D weight fracturing on an (8, 4) Galaxy  -  W_qkv",16))
    e.append(et(W_X,52,"WEIGHT  W_qkv [K, N]",12))
    e.append(et(W_X,68,"N cut 8 ways -> mesh axis 0",10,"#0b7285"))
    e.append(et(W_X,82,"K cut 4 ways -> mesh axis 1",10,"#e8590c"))
    for b in range(NB):
        for a in range(NA):
            hit=(a==HL_A and b==HL_B)
            e.append(er(W_X+a*CELL,W_Y+b*CELL,CELL,CELL,"#e8590c" if hit else "#adb5bd",
                        "#ffec99" if hit else "#f8f9fa",2 if hit else 1))
    e.append(et(X_X,232,"ACTIVATION  X [S, K]",12))
    e.append(et(X_X,248,"the SAME K cut, 4 ways -> mesh axis 1",10,"#e8590c"))
    for b in range(NB):
        hit=(b==HL_B)
        e.append(er(X_X+b*CELL,X_Y,CELL,96,"#e8590c" if hit else "#adb5bd",
                    "#ffec99" if hit else "#f8f9fa",2 if hit else 1))
        e.append(et(X_X+b*CELL+8,X_Y+102,f"b={b}",9,"#868e96"))
    e.append(et(X_X,X_Y+124,"K/4 per chip - replicated across all 8 chips of axis 0",9,"#868e96"))
    e.append(et(MESH_X,52,"THE MESH (8, 4)",12))
    e.append(et(MESH_X,68,"chip (a,b) holds block (a,b)",10,"#868e96"))
    mc=22
    for b in range(NB):
        for a in range(NA):
            hit=(a==HL_A and b==HL_B)
            e.append(er(MESH_X+a*mc,MESH_Y+b*mc,mc,mc,"#e8590c" if hit else "#adb5bd",
                        "#ffec99" if hit else "#ffffff",2 if hit else 1))
    e.append(el(MESH_X+HL_A*mc+mc/2,MESH_Y-6,MESH_X+HL_A*mc+mc/2,MESH_Y+NB*mc+4,"#e8590c",2))
    e.append(et(MESH_X+NA*mc+10,MESH_Y+NB*mc/2-6,"all_reduce\ncluster_axis=1\n4 chips only",10,"#e8590c"))
    e.append(et(40,392,"chip (a=2, b=1) computes",12))
    e.append(et(40,412,"X[:, bK/4 : (b+1)K/4]  x  W[bK/4:.. , aN/8:..]  =  partial Y [S, N/8]",12))
    e.append(et(40,432,"[S, K/4]                    [K/4, N/8]                 full width, quarter of the sum",9,"#868e96"))
    e.append(et(40,452,"-> all_reduce over the 4 chips sharing a=2 completes it",11,"#e8590c"))
    return dict(type="excalidraw",version=2,source="tt-learning/multichip",elements=e,
                appState={"gridSize":None,"viewBackgroundColor":"#ffffff"},files={})

if __name__=="__main__":
    import os
    here=os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here,"galaxy-2d.svg.frag"),"w").write(svg())
    json.dump(excalidraw(),open(os.path.join(here,"galaxy-2d.excalidraw"),"w"),indent=1)
    print("wrote galaxy-2d (.svg.frag + .excalidraw)")
