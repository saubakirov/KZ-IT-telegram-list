# Phase B evidence addendum — stale exact approval

The corrected owner authority validates structurally against the exact reviewed preview, but the mandatory fresh public-preview gate invalidates its use. The separate fresh probe retained in `../pre-apply-freshness/observations.json` covers all 28 candidates through the unchanged Phase A engine.

The deterministic comparison in `stale-approval-report.json` records changed response-body SHA-256 values for all 28 candidates and nine changed observed member counts. Six changed counts belong to approved ADD rows: `astana_hub` 13,572→13,568; `digitalbussinesskz` 8,362→8,361; `ethkz` 1,227→1,226; `it_jobs_kz` 9,702→9,703; `kolesa_group` 7,116→7,117; and `kz_bi_jobs` 5,479→5,478. Three changed counts belong to non-add rows: `helpfixit` 318→317; `itbazarkzchannel` 2,451→2,450; and `kazakhtelecom_official` 5,153→5,152.

Identity, target binding, visible name, peer type, and liveness classification remained stable, but the approved payload embeds the prior counts and evidence hashes. Under the explicit freshness/body/count binding, payload `a6e7444b3be13f6ed06f3268a079c2264001703ce8e83c83f14c65ab65c0dcac` and actions `c222aa49fb3481d1142380cf2636327ff73b486baed84af239cdf69ca0e41394` are stale and cannot be applied.

Result: **BLOCKED / FAIL CLOSED**. No controlled path was written; no pending marker or receipt was created. The reviewed preview, stage manifest, universe audit, and Reviewer readiness artifact remain byte-bound to canonical tip `c34d537c8d485b212a2fe275b8ab63783c980202`. A successor preview requires the Coordinator and the same Reviewer correction/readiness loop; it is not built here.
