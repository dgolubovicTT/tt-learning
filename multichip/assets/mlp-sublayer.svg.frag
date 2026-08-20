<svg viewBox="0 0 790 748" role="img" aria-label="The MLP sublayer as seven operations in a column, laid out the same way. The activation enters fractured, all_gather makes it gathered, rms_norm uses a replicated gamma. The w1 and w3 linears use column-cut weights of shape H by F over N cut at the same offsets, so both outputs are fractured on F identically. The SiLU multiply combines two operands with identical layout and moves no data. The w2 linear is row-cut with F as its contracted axis and produces a partial of shape S by H. reduce_scatter adds the partials and returns a fractured slice before the residual add.">
          <defs><marker id="mlp-sublayer-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker><marker id="mlp-sublayer-w" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="var(--muted)"/></marker></defs>
          <text x="270" y="16" font-family="ui-monospace, monospace" font-size="10" fill="var(--muted)" text-anchor="end" font-weight="600">ACTIVATION OUT</text>
          <text x="292" y="16" font-family="ui-monospace, monospace" font-size="10" fill="var(--muted)" text-anchor="start" font-weight="600">OPERATION</text>
          <text x="530" y="16" font-family="ui-monospace, monospace" font-size="10" fill="var(--muted)" text-anchor="start" font-weight="600">WEIGHT  ·  SECOND OPERAND</text>
          <text x="270" y="34" font-family="ui-monospace, monospace" font-size="11" fill="var(--ink)" text-anchor="end" font-weight="600">[S, H/N]   fractured</text>
          <line x1="399.0" y1="24" x2="399.0" y2="50" stroke="currentColor" stroke-width="1.5" marker-end="url(#mlp-sublayer-a)"/>
          <rect x="292" y="52" width="214" height="48" rx="3" fill="var(--ccl-wash)" stroke="var(--ccl)" stroke-width="2"/>
          <text x="399.0" y="81" font-family="ui-monospace, monospace" font-size="12.5" fill="var(--ink)" text-anchor="middle" font-weight="600">all_gather   dim=3</text>
          <text x="270" y="74" font-family="ui-monospace, monospace" font-size="11" fill="var(--ink)" text-anchor="end" font-weight="600">[S, H]</text>
          <text x="270" y="88" font-family="ui-monospace, monospace" font-size="10" fill="var(--ccl)" text-anchor="end">gathered</text>
          <line x1="399.0" y1="100" x2="399.0" y2="146" stroke="currentColor" stroke-width="1.5" marker-end="url(#mlp-sublayer-a)"/>
          <rect x="292" y="148" width="214" height="48" rx="3" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1.5"/>
          <text x="399.0" y="177" font-family="ui-monospace, monospace" font-size="12.5" fill="var(--ink)" text-anchor="middle" font-weight="600">rms_norm</text>
          <rect x="530" y="157.0" width="58" height="30" fill="none" stroke="var(--muted)" stroke-width="1.4"/><rect x="533" y="160.0" width="58" height="30" fill="none" stroke="var(--muted)" stroke-width="1" stroke-dasharray="3 2"/>
          <text x="596" y="166" font-family="ui-monospace, monospace" font-size="10" fill="var(--ink)" text-anchor="start">gamma   [H]</text>
          <text x="596" y="180" font-family="ui-monospace, monospace" font-size="9.5" fill="var(--muted)" text-anchor="start">replicated on every chip</text>
          <text x="530" y="199.0" font-family="ui-monospace, monospace" font-size="9.5" fill="var(--muted)" text-anchor="start" font-weight="600">replicated</text>
          <line x1="516" y1="172.0" x2="510" y2="172.0" stroke="var(--muted)" stroke-width="1.2" marker-end="url(#mlp-sublayer-w)"/>
          <text x="270" y="170" font-family="ui-monospace, monospace" font-size="11" fill="var(--ink)" text-anchor="end" font-weight="600">[S, H]</text>
          <text x="270" y="184" font-family="ui-monospace, monospace" font-size="10" fill="var(--ccl)" text-anchor="end">gathered</text>
          <line x1="399.0" y1="196" x2="399.0" y2="242" stroke="currentColor" stroke-width="1.5" marker-end="url(#mlp-sublayer-a)"/>
          <rect x="292" y="244" width="214" height="48" rx="3" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1.5"/>
          <text x="399.0" y="273" font-family="ui-monospace, monospace" font-size="12.5" fill="var(--ink)" text-anchor="middle" font-weight="600">linear   w1, w3</text>
          <rect x="530" y="253.0" width="58" height="30" fill="none" stroke="var(--local)" stroke-width="1.4"/><line x1="544.5" y1="253.0" x2="544.5" y2="283.0" stroke="var(--local)" stroke-width="1"/><line x1="559.0" y1="253.0" x2="559.0" y2="283.0" stroke="var(--local)" stroke-width="1"/><line x1="573.5" y1="253.0" x2="573.5" y2="283.0" stroke="var(--local)" stroke-width="1"/><rect x="530" y="253.0" width="14.5" height="30" fill="var(--local)" opacity="0.28"/>
          <text x="596" y="262" font-family="ui-monospace, monospace" font-size="10" fill="var(--ink)" text-anchor="start">w1, w3   [H, F/N]</text>
          <text x="596" y="276" font-family="ui-monospace, monospace" font-size="9.5" fill="var(--muted)" text-anchor="start">both cut at the same offsets</text>
          <text x="530" y="295.0" font-family="ui-monospace, monospace" font-size="9.5" fill="var(--local)" text-anchor="start" font-weight="600">column-cut</text>
          <line x1="516" y1="268.0" x2="510" y2="268.0" stroke="var(--muted)" stroke-width="1.2" marker-end="url(#mlp-sublayer-w)"/>
          <text x="270" y="266" font-family="ui-monospace, monospace" font-size="11" fill="var(--ink)" text-anchor="end" font-weight="600">[S, F/N]  &#215;2</text>
          <text x="270" y="280" font-family="ui-monospace, monospace" font-size="10" fill="var(--ink-2)" text-anchor="end">fractured on F</text>
          <text x="270" y="294" font-family="ui-monospace, monospace" font-size="9" fill="var(--muted)" text-anchor="end">F = 28672 vs H = 8192 for Llama-70B</text>
          <line x1="399.0" y1="292" x2="399.0" y2="338" stroke="currentColor" stroke-width="1.5" marker-end="url(#mlp-sublayer-a)"/>
          <rect x="292" y="340" width="214" height="48" rx="3" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1.5"/>
          <text x="399.0" y="369" font-family="ui-monospace, monospace" font-size="12.5" fill="var(--ink)" text-anchor="middle" font-weight="600">mul   SiLU(w1) &#215; w3</text>
          <text x="270" y="362" font-family="ui-monospace, monospace" font-size="11" fill="var(--ink)" text-anchor="end" font-weight="600">[S, F/N]</text>
          <text x="270" y="376" font-family="ui-monospace, monospace" font-size="10" fill="var(--ink-2)" text-anchor="end">fractured on F</text>
          <text x="270" y="390" font-family="ui-monospace, monospace" font-size="9" fill="var(--muted)" text-anchor="end">two operands, identical layout - elementwise</text>
          <line x1="399.0" y1="388" x2="399.0" y2="434" stroke="currentColor" stroke-width="1.5" marker-end="url(#mlp-sublayer-a)"/>
          <rect x="292" y="436" width="214" height="48" rx="3" fill="var(--surface-2)" stroke="var(--rule)" stroke-width="1.5"/>
          <text x="399.0" y="465" font-family="ui-monospace, monospace" font-size="12.5" fill="var(--ink)" text-anchor="middle" font-weight="600">linear   w2</text>
          <rect x="530" y="445.0" width="58" height="30" fill="none" stroke="var(--ccl)" stroke-width="1.4"/><line x1="530" y1="452.5" x2="588" y2="452.5" stroke="var(--ccl)" stroke-width="1"/><line x1="530" y1="460.0" x2="588" y2="460.0" stroke="var(--ccl)" stroke-width="1"/><line x1="530" y1="467.5" x2="588" y2="467.5" stroke="var(--ccl)" stroke-width="1"/><rect x="530" y="445.0" width="58" height="7.5" fill="var(--ccl)" opacity="0.28"/>
          <text x="596" y="454" font-family="ui-monospace, monospace" font-size="10" fill="var(--ink)" text-anchor="start">w2   [F/N, H]</text>
          <text x="596" y="468" font-family="ui-monospace, monospace" font-size="9.5" fill="var(--muted)" text-anchor="start">F is now the contracted axis</text>
          <text x="530" y="487.0" font-family="ui-monospace, monospace" font-size="9.5" fill="var(--ccl)" text-anchor="start" font-weight="600">row-cut</text>
          <line x1="516" y1="460.0" x2="510" y2="460.0" stroke="var(--muted)" stroke-width="1.2" marker-end="url(#mlp-sublayer-w)"/>
          <text x="270" y="458" font-family="ui-monospace, monospace" font-size="11" fill="var(--ink)" text-anchor="end" font-weight="600">[S, H]</text>
          <text x="270" y="472" font-family="ui-monospace, monospace" font-size="10" fill="var(--ccl)" text-anchor="end" font-weight="600">PARTIAL</text>
          <text x="270" y="486" font-family="ui-monospace, monospace" font-size="9" fill="var(--muted)" text-anchor="end">full shape, only this chip's terms of the sum</text>
          <line x1="399.0" y1="484" x2="399.0" y2="530" stroke="currentColor" stroke-width="1.5" marker-end="url(#mlp-sublayer-a)"/>
          <rect x="292" y="532" width="214" height="48" rx="3" fill="var(--ccl-wash)" stroke="var(--ccl)" stroke-width="2"/>
          <text x="399.0" y="561" font-family="ui-monospace, monospace" font-size="12.5" fill="var(--ink)" text-anchor="middle" font-weight="600">reduce_scatter   dim=3</text>
          <text x="270" y="554" font-family="ui-monospace, monospace" font-size="11" fill="var(--ink)" text-anchor="end" font-weight="600">[S, H/N]</text>
          <text x="270" y="568" font-family="ui-monospace, monospace" font-size="10" fill="var(--ink-2)" text-anchor="end">fractured</text>
          <text x="270" y="582" font-family="ui-monospace, monospace" font-size="9" fill="var(--muted)" text-anchor="end">adds the partials, keeps one slice</text>
          <line x1="399.0" y1="580" x2="399.0" y2="626" stroke="currentColor" stroke-width="1.5" marker-end="url(#mlp-sublayer-a)"/>
          <rect x="292" y="628" width="214" height="48" rx="3" fill="var(--surface)" stroke="var(--resid)" stroke-width="1.5"/>
          <text x="399.0" y="657" font-family="ui-monospace, monospace" font-size="12.5" fill="var(--ink)" text-anchor="middle" font-weight="600">add   residual</text>
          <text x="530" y="648" font-family="ui-monospace, monospace" font-size="10" fill="var(--resid)" text-anchor="start">residual   [S, H/N]</text>
          <text x="530" y="662" font-family="ui-monospace, monospace" font-size="9.5" fill="var(--muted)" text-anchor="start">same layout on both sides</text>
          <line x1="516" y1="652.0" x2="510" y2="652.0" stroke="var(--muted)" stroke-width="1.2" marker-end="url(#mlp-sublayer-w)"/>
          <text x="270" y="650" font-family="ui-monospace, monospace" font-size="11" fill="var(--ink)" text-anchor="end" font-weight="600">[S, H/N]</text>
          <text x="270" y="664" font-family="ui-monospace, monospace" font-size="10" fill="var(--ink-2)" text-anchor="end">fractured</text>
          </svg>