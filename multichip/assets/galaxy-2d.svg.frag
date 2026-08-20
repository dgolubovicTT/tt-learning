<svg viewBox="0 0 880 470" role="img" aria-label="Two-D weight fracturing on an eight by four Galaxy. The weight W_qkv of shape K by N is drawn as a grid of four rows by eight columns: N is cut eight ways along mesh axis 0 and K is cut four ways along mesh axis 1. The activation X of shape S by K is cut along K in exactly the same four places, and each slice is replicated across all eight chips of axis 0. Slice b of the activation meets row b of the weight. The mesh itself has the same eight by four shape, so chip a,b simply holds block a,b. One chip multiplies an S by K over four activation slice with a K over four by N over eight weight block, giving a full-width but partial output, and an all_reduce down the four chips of a mesh column completes the sum.">
          <defs><marker id="g2a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker><marker id="g2r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="var(--ccl)"/></marker></defs>
          <text x="246" y="34" font-family="ui-monospace, monospace" font-size="11" fill="var(--ink)" text-anchor="start" font-weight="600">WEIGHT   W_qkv  [K, N]</text>
          <text x="246" y="50" font-family="ui-monospace, monospace" font-size="9.5" fill="var(--local)" text-anchor="start">N = qkv width, cut 8 ways  →  mesh axis 0</text>
          <text x="246" y="62" font-family="ui-monospace, monospace" font-size="9.5" fill="var(--ccl)" text-anchor="start">K = H,         cut 4 ways  →  mesh axis 1</text>
          <rect x="246" y="78" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="280" y="78" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="314" y="78" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="348" y="78" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="382" y="78" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="416" y="78" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="450" y="78" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="484" y="78" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="246" y="112" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="280" y="112" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="314" y="112" width="34" height="34" fill="var(--ccl-wash)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="314" y="112" width="34" height="34" fill="none" stroke="var(--ccl)" stroke-width="2.5"/>
          <rect x="348" y="112" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="382" y="112" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="416" y="112" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="450" y="112" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="484" y="112" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="246" y="146" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="280" y="146" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="314" y="146" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="348" y="146" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="382" y="146" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="416" y="146" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="450" y="146" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="484" y="146" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="246" y="180" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="280" y="180" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="314" y="180" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="348" y="180" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="382" y="180" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="416" y="180" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="450" y="180" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="484" y="180" width="34" height="34" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <line x1="246" y1="70" x2="518" y2="70" stroke="var(--local)" stroke-width="1.2" marker-end="url(#g2a)"/>
          <text x="524" y="228" font-family="ui-monospace, monospace" font-size="9" fill="var(--local)" text-anchor="start">N / 8 per chip</text>
          <text x="236" y="146.0" font-family="ui-monospace, monospace" font-size="9.5" fill="var(--ccl)" text-anchor="middle" transform="rotate(-90 236 146.0)">K / 4</text>
          <text x="40" y="232" font-family="ui-monospace, monospace" font-size="11" fill="var(--ink)" text-anchor="start" font-weight="600">ACTIVATION   X  [S, K]</text>
          <text x="40" y="248" font-family="ui-monospace, monospace" font-size="9.5" fill="var(--ccl)" text-anchor="start">the SAME K cut, 4 ways → mesh axis 1</text>
          <rect x="40" y="256" width="34" height="96" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <text x="57.0" y="365" font-family="ui-monospace, monospace" font-size="9" fill="var(--muted)" text-anchor="middle">b=0</text>
          <rect x="74" y="256" width="34" height="96" fill="var(--ccl-wash)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="74" y="256" width="34" height="96" fill="none" stroke="var(--ccl)" stroke-width="2.5"/>
          <text x="91.0" y="365" font-family="ui-monospace, monospace" font-size="9" fill="var(--ccl)" text-anchor="middle">b=1</text>
          <rect x="108" y="256" width="34" height="96" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <text x="125.0" y="365" font-family="ui-monospace, monospace" font-size="9" fill="var(--muted)" text-anchor="middle">b=2</text>
          <rect x="142" y="256" width="34" height="96" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1"/>
          <text x="159.0" y="365" font-family="ui-monospace, monospace" font-size="9" fill="var(--muted)" text-anchor="middle">b=3</text>
          <text x="40" y="380" font-family="ui-monospace, monospace" font-size="9" fill="var(--muted)" text-anchor="start">K / 4 per chip · replicated across all 8 chips of axis 0</text>
          <text x="32" y="304" font-family="ui-monospace, monospace" font-size="9.5" fill="currentColor" text-anchor="middle">S</text>
          <path d="M 91.0 252 L 91.0 236 L 224 236 L 224 129.0 L 242 129.0" stroke="var(--ccl)" stroke-width="1.5" fill="none" stroke-dasharray="4 3" marker-end="url(#g2r)"/>
          <text x="190" y="232" font-family="ui-monospace, monospace" font-size="9" fill="var(--ccl)" text-anchor="start">slice b of X meets row b of W</text>
          <text x="610" y="34" font-family="ui-monospace, monospace" font-size="11" fill="var(--ink)" text-anchor="start" font-weight="600">THE MESH  (8, 4)</text>
          <text x="610" y="50" font-family="ui-monospace, monospace" font-size="9.5" fill="var(--muted)" text-anchor="start">same grid — chip (a,b) holds block (a,b)</text>
          <rect x="610" y="78" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="632" y="78" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="654" y="78" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="676" y="78" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="698" y="78" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="720" y="78" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="742" y="78" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="764" y="78" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="610" y="100" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="632" y="100" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="654" y="100" width="22" height="22" fill="var(--ccl-wash)" stroke="var(--ccl)" stroke-width="2"/>
          <rect x="676" y="100" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="698" y="100" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="720" y="100" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="742" y="100" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="764" y="100" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="610" y="122" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="632" y="122" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="654" y="122" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="676" y="122" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="698" y="122" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="720" y="122" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="742" y="122" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="764" y="122" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="610" y="144" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="632" y="144" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="654" y="144" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="676" y="144" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="698" y="144" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="720" y="144" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="742" y="144" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <rect x="764" y="144" width="22" height="22" fill="var(--surface)" stroke="var(--rule)" stroke-width="1"/>
          <text x="610" y="182" font-family="ui-monospace, monospace" font-size="9" fill="var(--local)" text-anchor="start">a → axis 0, 8 chips</text>
          <text x="610" y="194" font-family="ui-monospace, monospace" font-size="9" fill="var(--ccl)" text-anchor="start">b ↓ axis 1, 4 chips</text>
          <line x1="665.0" y1="72" x2="665.0" y2="170" stroke="var(--ccl)" stroke-width="2" marker-end="url(#g2r)"/>
          <text x="796" y="122.0" font-family="ui-monospace, monospace" font-size="9.5" fill="var(--ccl)" text-anchor="start" font-weight="600">all_reduce</text>
          <text x="796" y="135.0" font-family="ui-monospace, monospace" font-size="9.5" fill="var(--ccl)" text-anchor="start">cluster_axis=1</text>
          <text x="796" y="148.0" font-family="ui-monospace, monospace" font-size="9" fill="var(--muted)" text-anchor="start">4 chips only</text>
          <line x1="40" y1="384" x2="840" y2="384" stroke="var(--rule)" stroke-width="1"/>
          <text x="40" y="402" font-family="ui-monospace, monospace" font-size="10.5" fill="var(--ink)" text-anchor="start" font-weight="600">chip (a=2, b=1) computes</text>
          <text x="40" y="420" font-family="ui-monospace, monospace" font-size="11" fill="var(--ink)" text-anchor="start">X[:, b·K/4 : (b+1)·K/4]   ×   W[b·K/4 : … ,  a·N/8 : …]   =   partial Y  [S, N/8]</text>
          <text x="40" y="438" font-family="ui-monospace, monospace" font-size="9" fill="var(--muted)" text-anchor="start">[S, K/4]                         [K/4, N/8]                    full N/8 width, only this chip’s quarter of the sum</text>
          <text x="40" y="458" font-family="ui-monospace, monospace" font-size="10" fill="var(--ccl)" text-anchor="start">→ all_reduce over the 4 chips sharing a=2 completes the sum. Output stays cut 8 ways on axis 0.</text>
          </svg>