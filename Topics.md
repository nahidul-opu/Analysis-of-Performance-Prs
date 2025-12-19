# Performance Topics Reference (with PR Counts)

Total number of performance PRs: **1221**.

Each topic includes its PR count and share of the entire performance dataset.

## Topic 0: CI/CD Workflow (96 PRs, 7.9%)

**Topic Number:** 0
**Topic Name:** CI/CD Workflow
**Topic Definition:** Pull requests that streamline or speed up continuous integration and delivery workflows, such as optimizing jobs, caching, or pipeline structure.
**Number of PRs in this topic:** 96 (7.9% of all performance PRs)
**Examples:**
1. **PR ID:** 448
   - **Title:** Add GitHub API caching to prevent rate limiting
   - **Description summary:** - Create GitHub API caching script that handles authenticated and unauthenticated requests - Update Dockerfile to include the script in the container - Update init-firewall.sh to use cached GitHub API data - Modify devcontainer.json to run cache script before build...
1. **PR ID:** 110
   - **Title:** Add vcpkg dependency caching to Windows CI workflow
   - **Description summary:** ## Overview This PR implements vcpkg dependency caching for the Windows CI workflow to significantly speed up build times by avoiding full dependency rebuilds on every CI run. ## Changes Added a comprehensive caching strategy to `.github/workflows/ci-windows-minimal.yml` that: 1. **Caches...

## Topic 1: Transpiler Becnhmarking (56 PRs, 4.6%)

**Topic Number:** 1
**Topic Name:** Transpiler Becnhmarking
**Topic Definition:** Pull requests that add or refine benchmarks specifically targeting transpilers and generated code, to measure and compare performance across configurations.
**Number of PRs in this topic:** 56 (4.6% of all performance PRs)
**Examples:**
1. **PR ID:** 12942
   - **Title:** Update Java benchmark handling
   - **Description summary:** ## Summary - adjust benchmark env parsing for Java tests - regenerate Java rosetta outputs with benchmark info - update docs and progress tables ## Testing - `UPDATE=1 MOCHI_BENCHMARK=1 go test -tags slow ./transpiler/x/java -run Rosetta -index 1 -count=1` ------...
1. **PR ID:** 12955
   - **Title:** Add benchmark support for transpiler and VM tests
   - **Description summary:** ## Summary - allow wrapping generated main in benchmark block via `benchMainFlag` - record benchmark outputs for Go transpiler examples - support Rosetta benchmarking in the VM tests - generate VM Rosetta checklist with durations and memory usage ## Testing...

## Topic 2: UI Data-loading and Rendering (51 PRs, 4.2%)

**Topic Number:** 2
**Topic Name:** UI Data-loading and Rendering
**Topic Definition:** Pull requests that make user interfaces fetch data more efficiently and render screens faster, reducing perceived load times.
**Number of PRs in this topic:** 51 (4.2% of all performance PRs)
**Examples:**
1. **PR ID:** 1037
   - **Title:** feat: implement comprehensive species tracking system with seasonal/yearly detection badges
   - **Description summary:** ## Summary This PR implements a comprehensive species tracking system that displays visual badges on the DailySummaryCard to indicate when species are new, new this year, or new this season. The implementation includes proper database queries, caching, and UI enhancements....
1. **PR ID:** 506
   - **Title:** [WIP] Avoid reopening /dev/kvm or /dev/mshv for every new sandbox
   - **Description summary:** Thanks for assigning this issue to me. I'm starting to work on it and will keep this PR's description up to date as I form a plan and make progress. Original issue description: > We should just reuse the same...

## Topic 3: TTL approximation (43 PRs, 3.5%)

**Topic Number:** 3
**Topic Name:** TTL approximation
**Topic Definition:** Pull requests that approximate or tune time-to-live and expiry semantics so caches remain effective without being too stale or too aggressive.
**Number of PRs in this topic:** 43 (3.5% of all performance PRs)
**Examples:**
1. **PR ID:** 5
   - **Title:** Fix performance and lock issues with fine-grained locking strategy
   - **Description summary:** ## Problem The vocal agent had critical performance and concurrency issues due to coarse-grained locking: - **Blocking Pipeline**: Single `tts_lock` held for entire TTS pipeline (response generation + audio processing + playback) - **Unnecessary STT Interruption**: Speech-to-text was paused during...
1. **PR ID:** 9510
   - **Title:** Make EnvironmentStatistics CPU usage collection interval configurable
   - **Description summary:** Currently, the CPU usage collection interval in `EnvironmentStatisticsProvider` is hardcoded to 1 second, which can impact other EventListener implementations such as Application Insights. This PR makes the CPU usage collection interval configurable by: 1. Adding a new `EnvironmentStatisticsOptions` class with...

## Topic 4: Sequence Data Processing (40 PRs, 3.3%)

**Topic Number:** 4
**Topic Name:** Sequence Data Processing
**Topic Definition:** Pull requests that focus on efficient processing of ordered or sequential datasets, such as time series or event streams.
**Number of PRs in this topic:** 40 (3.3% of all performance PRs)
**Examples:**
1. **PR ID:** 59071
   - **Title:** skip unnecessary alias-check in collect(::AbstractArray) from copyto\!
   - **Description summary:** As discussed on Slack with @MasonProtter & @jakobnissen, `collect` currently does a usually cheap - but sometimes expensive - aliasing check (via `unalias`->`mightalias`->`dataid` -> `objectid`) before copying contents over; this check is unnecessary, however, since the source array is newly...
1. **PR ID:** 2255
   - **Title:** Optimize BigInt hex conversion
   - **Description summary:** ## Summary - improve `BigInt::to_hex` performance by using `StringBuilder` ## Testing - `moon info` - `moon test` *(fails: no output)* ------ https://chatgpt.com/codex/tasks/task_e_68499a1746208320b6d98eb4cbce0581

## Topic 5: Join Query (35 PRs, 2.9%)

**Topic Number:** 5
**Topic Name:** Join Query
**Topic Definition:** Pull requests that optimize join operations between datasets or tables, improving latency and resource usage for relational-style queries.
**Number of PRs in this topic:** 35 (2.9% of all performance PRs)
**Examples:**
1. **PR ID:** 3924
   - **Title:** Improve join optimization
   - **Description summary:** ## Summary - detect more equality cases in join condition, handling `+0`/`-0` - benchmark join with `+0` arithmetic to verify optimization ## Testing - `go test ./... -count=1` ------ https://chatgpt.com/codex/tasks/task_e_685f6f460e188320906298a7c44ae3ad
1. **PR ID:** 9455
   - **Title:** Improve PHP join compilation
   - **Description summary:** ## Summary - compile left_join_multi/right_join/outer_join queries without `_query` - note PHP join improvements in README ## Testing - `go test ./compiler/x/php -run TestPHPCompiler_VMValid_Golden -count=1 -tags=slow` ------ https://chatgpt.com/codex/tasks/task_e_6879bc3a2b708320b51e0b494bd2c734

## Topic 6: Networking & I/O (32 PRs, 2.6%)

**Topic Number:** 6
**Topic Name:** Networking & I/O
**Topic Definition:** Pull requests that improve network and I/O performance, for example by reducing round-trips, batching operations, or tuning buffering.
**Number of PRs in this topic:** 32 (2.6% of all performance PRs)
**Examples:**
1. **PR ID:** 17613
   - **Title:** stm32/eth: Improve Ethernet driver with link detection and static IP support.
   - **Description summary:** ## Summary This PR implements comprehensive improvements to the STM32 Ethernet driver, addressing several critical usability issues and adding important features for robust network connectivity. **Key improvements:** - ✅ Automatic cable connect/disconnect detection with proper LWIP integration - ✅ Fixed...
1. **PR ID:** 38838
   - **Title:** Fix GitHub API rate limiting in chess workflow by replacing API calls with local file storage
   - **Description summary:** ## Problem The chess game workflow was experiencing rate limiting issues due to excessive GitHub API calls. Every time a move was made, the workflow would call `@octokit.list_issues()` to: 1. Check if the same user made the previous move (consecutive...

## Topic 7: Dependency Management (32 PRs, 2.6%)

**Topic Number:** 7
**Topic Name:** Dependency Management
**Topic Definition:** Pull requests that adjust dependency graphs, versions, or resolution strategies to improve build speed, stability, and runtime performance.
**Number of PRs in this topic:** 32 (2.6% of all performance PRs)
**Examples:**
1. **PR ID:** 5375
   - **Title:** docs: Upgrade Docusaurus from 3.7.0 to 3.8.1
   - **Description summary:** This PR upgrades Docusaurus dependencies from version 3.7.0 to 3.8.1 (latest stable) to improve performance, security, and provide access to the latest features and bug fixes. ## Changes Made ### 📦 Dependencies Updated - `@docusaurus/core`: 3.7.0 → 3.8.1 - `@docusaurus/plugin-content-blog`:...
1. **PR ID:** 5403
   - **Title:** Update remotion.dev/convert to Tailwind 4
   - **Description summary:** Upgraded `packages/convert` from Tailwind CSS v3.4.13 to v4.1.1, following the same pattern used in `packages/promo-pages`. ## Changes Made - **Dependencies**: Updated to Tailwind 4.1.1 with `@tailwindcss/cli` and `@tailwindcss/vite` - **CSS Migration**: Converted `app/tailwind.css` from v3 to v4 syntax: - Replaced...

## Topic 8: Performance Benchmarking (30 PRs, 2.5%)

**Topic Number:** 8
**Topic Name:** Performance Benchmarking
**Topic Definition:** Pull requests that introduce or refine performance benchmarks to track regressions and improvements over time.
**Number of PRs in this topic:** 30 (2.5% of all performance PRs)
**Examples:**
1. **PR ID:** 60
   - **Title:** feat: Phase 7.1 - Basket Asset Performance Tracking
   - **Description summary:** ## Summary This PR implements Phase 7.1 of the roadmap - Basket Asset Performance Tracking. This adds comprehensive performance analytics for basket assets including returns, volatility, Sharpe ratio, and maximum drawdown calculations. ## What's Changed ### Models & Database -...
1. **PR ID:** 584
   - **Title:** Implement ForestRun performance benchmark system with GitHub Actions
   - **Description summary:** Implements a comprehensive performance benchmark system for the ForestRun cache to measure and compare cache operation performance against Apollo's InMemoryCache. ## Features ### 🚀 Performance Benchmarks - **Read Operations**: Cache read performance comparison - **Write Operations**: Cache write performance measurement...

## Topic 9: Memory Leak (28 PRs, 2.3%)

**Topic Number:** 9
**Topic Name:** Memory Leak
**Topic Definition:** Pull requests that detect and fix memory leaks or unbounded memory growth in long-running processes or hot paths.
**Number of PRs in this topic:** 28 (2.3% of all performance PRs)
**Examples:**
1. **PR ID:** 83
   - **Title:** fix: memory leaks and server stability issues
   - **Description summary:** ## Summary This PR addresses critical memory leaks and stability issues in the Zen MCP server that were causing server crashes during heavy usage, requiring frequent reinstallation. ### Fixed Issues - **Memory leaks in GeminiModelProvider**: Added bounded token cache with...
1. **PR ID:** 9278
   - **Title:** fix(tabs): resolve memory leak caused by animation transitions
   - **Description summary:** ## Problem The nz-tabset component was experiencing memory leaks where detached DOM elements accumulated in memory when tabs were repeatedly created and destroyed. As shown in the memory snapshot below, multiple detached `<nz-tabset>` elements were being retained: ![Memory leak showing...

## Topic 10: Constant Folding (25 PRs, 2.0%)

**Topic Number:** 10
**Topic Name:** Constant Folding
**Topic Definition:** Pull requests that enhance constant folding in compilers or VMs, evaluating expressions at compile time to produce faster runtime code.
**Number of PRs in this topic:** 25 (2.0% of all performance PRs)
**Examples:**
1. **PR ID:** 213
   - **Title:** Improve interpreter const-eval
   - **Description summary:** ## Summary - support const-evaluation of pure function calls directly in the interpreter - avoid recursion by disabling pure evaluation when invoked from `EvalPureCall` ## Testing - `go test ./... --vet=off -v` ------ https://chatgpt.com/codex/tasks/task_e_684633d1eab483209e2372d231591902
1. **PR ID:** 222
   - **Title:** Enable AOT folding in interpreter
   - **Description summary:** ## Summary - add `FoldPureCalls` for ahead-of-time constant folding - expose folding via `--aot` flag in CLI and use it in benchmarks - move TS runtime helpers before program execution - update test outputs for new TypeScript layout ## Testing...

## Topic 11: CLI tool (24 PRs, 2.0%)

**Topic Number:** 11
**Topic Name:** CLI tool
**Topic Definition:** Pull requests that improve the performance or responsiveness of command-line tools, such as faster startup, reduced I/O, or better caching.
**Number of PRs in this topic:** 24 (2.0% of all performance PRs)
**Examples:**
1. **PR ID:** 19
   - **Title:** Replace CLI subprocess approach with Claude Code SDK
   - **Description summary:** ## Description Replace the current CLI subprocess execution approach with the Claude Code SDK for better performance, type safety, and error handling. This is a clean replacement that maintains the same interface while providing significant performance improvements. ## Type of...
1. **PR ID:** 4304
   - **Title:** Implement lazy loading for RegistryInstance to improve latency in operations where the registry does not need to be read
   - **Description summary:** 👨 Before: ``` julia> @time Pkg.instantiate() 0.390297 seconds (1.95 M allocations: 148.381 MiB, 16.29% gc time, 31.03% compilation time: 68% of which was recompilation) ``` After: ``` julia> @time Pkg.instantiate() 0.161872 seconds (456.14 k allocations: 27.898 MiB, 9.75% gc time,...

## Topic 12: UI loading and Rendering (23 PRs, 1.9%)

**Topic Number:** 12
**Topic Name:** UI loading and Rendering
**Topic Definition:** Pull requests that make user interfaces fetch data more efficiently and render screens faster, reducing perceived load times.
**Number of PRs in this topic:** 23 (1.9% of all performance PRs)
**Examples:**
1. **PR ID:** 7904
   - **Title:** Fix cache not being used when scopes are empty in acquireTokenSilent
   - **Description summary:** ## Problem When `acquireTokenSilent` is called with empty scopes (`scopes: []`), the cache lookup fails with a configuration error, causing unnecessary network requests to Azure AD instead of using cached tokens. ```javascript import { useAccount, useMsal } from '@azure/msal-react'; const...
1. **PR ID:** 3409
   - **Title:** Add high-performance loggers to credential providers
   - **Description summary:** ## Summary This PR replaces ad-hoc logging code with high-performance loggers using the `LoggerMessage.Define` pattern in credential providers, as requested in the feature request. ## Changes Made ### Files Updated - **`OidcIdpSignedAssertionProvider.cs`** - Made class `partial` and replaced 3 direct...

## Topic 13: Evaluation tooling (23 PRs, 1.9%)

**Topic Number:** 13
**Topic Name:** Evaluation tooling
**Topic Definition:** Pull requests that improve the infrastructure used to evaluate systems, including metrics collection, scoring, and experiment tracking.
**Number of PRs in this topic:** 23 (1.9% of all performance PRs)
**Examples:**
1. **PR ID:** 3678
   - **Title:** fix duplicate d3 in Insight PWA
   - **Description summary:** ## Summary - avoid bundling d3 in insight.bundle.js - keep d3 script tag in generated Insight docs ## Testing - `pre-commit run --files alpha_factory_v1/demos/alpha_agi_insight_v1/insight_browser_v1/build.js docs/alpha_agi_insight_v1/index.html` - `python check_env.py --auto-install` - `python scripts/verify_insight_offline.py` *(fails: integrity check for insight.bundle.js)* ------ https://chatgpt.com/codex/tasks/task_e_68802ac9e95083339f0f080d4f47f106
1. **PR ID:** 2532
   - **Title:** [alpha_factory] document placeholder and add cycle heuristic
   - **Description summary:** ## Summary - mark evaluate_agent placeholder in docs - mention placeholder behaviour in changelog - tweak MetaRefinementAgent to detect slow cycles - test cycle adjustment heuristic ## Testing - `pre-commit run --files alpha_factory_v1/core/agents/meta_refinement_agent.py docs/ARCHITECTURE.md docs/CHANGELOG.md tests/test_meta_refinement_agent.py` *(fails: proto-verify; verify-requirements-lock)* -...

## Topic 14: Compiler collection handling (23 PRs, 1.9%)

**Topic Number:** 14
**Topic Name:** Compiler collection handling
**Topic Definition:** Pull requests that refine how compilers represent, transform, or optimize collections such as lists, arrays, and maps.
**Number of PRs in this topic:** 23 (1.9% of all performance PRs)
**Examples:**
1. **PR ID:** 9343
   - **Title:** Improve Fortran constant list folding
   - **Description summary:** ## Summary - add constant list propagation to the Fortran compiler - fold `len`, `count`, `append`, `union`, `except`, etc. when lists are stored in variables - document new capability in `tests/machine/x/fortran/README.md` - record progress in `compiler/x/fortran/TASKS.md` ## Testing - `go...
1. **PR ID:** 9363
   - **Title:** Improve Fortran constant folding
   - **Description summary:** ## Summary - enhance Fortran compiler constant folding - fold `len` for constant strings - document new optimization in README and TASKS ## Testing - `go test ./...` ------ https://chatgpt.com/codex/tasks/task_e_6879243a44f48320af68a4631a1439b9

## Topic 15: VM Constant Folding (22 PRs, 1.8%)

**Topic Number:** 15
**Topic Name:** VM Constant Folding
**Topic Definition:** Pull requests that enhance constant folding in compilers or VMs, evaluating expressions at compile time to produce faster runtime code.
**Number of PRs in this topic:** 22 (1.8% of all performance PRs)
**Examples:**
1. **PR ID:** 4261
   - **Title:** Update lower builtin folding and TPC-DS IR outputs
   - **Description summary:** ## Summary - support constant folding for `lower` builtin in the VM compiler - regenerate IR output for TPC‑DS queries q50–q59 to reflect the updated compiler behavior ## Testing - `go test ./...` ------ https://chatgpt.com/codex/tasks/task_e_6862aa0298588320bdee85ae21c4f291
1. **PR ID:** 4268
   - **Title:** Update vm reverse folding
   - **Description summary:** ## Summary - fold constant `reverse` calls at compile time - refresh IR golden for tpc-ds q8 ## Testing - `go test -tags slow ./tests/vm -run "TPCDS/q[1-9]\.mochi$" -count=1` ------ https://chatgpt.com/codex/tasks/task_e_6862aeaf410c8320af622849dc372d40

## Topic 16: LLM Token Usage (22 PRs, 1.8%)

**Topic Number:** 16
**Topic Name:** LLM Token Usage
**Topic Definition:** Pull requests that reduce token consumption or latency for large language model calls while preserving or improving output quality.
**Number of PRs in this topic:** 22 (1.8% of all performance PRs)
**Examples:**
1. **PR ID:** 147
   - **Title:** feat: Add support for multiple tool calls in a single message
   - **Description summary:** ## Description <\!-- Provide a brief description of the changes in this PR --> This PR adds support for executing multiple tool calls within a single message, significantly improving efficiency for tool-based environments and agent workflows. Agents can now make...
1. **PR ID:** 2085
   - **Title:** Create PR to deactivate thinking field
   - **Description summary:** The browser-use agent's "thinking" field can now be optionally deactivated. Key changes include: * A `disable_thinking: bool = False` parameter was added to the `Agent` class in `browser_use/agent/service.py`, defaulting to `False` for backward compatibility. * The `SystemPrompt` in `browser_use/agent/prompts.py` was...

## Topic 17: Build Performance (21 PRs, 1.7%)

**Topic Number:** 17
**Topic Name:** Build Performance
**Topic Definition:** Pull requests that directly target build performance, such as parallelization, incremental builds, or cache reuse.
**Number of PRs in this topic:** 21 (1.7% of all performance PRs)
**Examples:**
1. **PR ID:** 253
   - **Title:** build: Add optional build tags to reduce binary size
   - **Description summary:** This PR implements conditional compilation using Go build tags to make optional features truly optional, allowing users to choose between a smaller binary and full functionality. ## Results | Build Configuration | Binary Size | Reduction | |---------------------|-------------|-----------| | Original...
1. **PR ID:** 2406
   - **Title:** Remove testing libraries from production environments
   - **Description summary:** This PR addresses the issue of testing libraries being included in production builds, which unnecessarily increases binary size. ## Problem The `github.com/stretchr/testify` library was being imported by non-test files, causing it to be included in production builds even though it's...

## Topic 18: Compiler Runtine (21 PRs, 1.7%)

**Topic Number:** 18
**Topic Name:** Compiler Runtine
**Topic Definition:** Pull requests that optimize runtime behavior in compiled programs or virtual machines, including dispatch, allocation, and execution paths.
**Number of PRs in this topic:** 21 (1.7% of all performance PRs)
**Examples:**
1. **PR ID:** 4363
   - **Title:** Primitives for raw OCaml block access
   - **Description summary:** ## Summary This PR extracts the Flambda2 parts of the block indices work from PR #4017 (rtjoa.block-indices). It adds two new primitives that will enable faster field access in unusual use cases, similar to Obj.raw_field but with better performance. ##...
1. **PR ID:** 7040
   - **Title:** Add conditional runtime emission to OCaml compiler
   - **Description summary:** ## Summary - enhance OCaml backend with feature scanning - emit runtime helpers only when required by a program ## Testing - `go vet ./...` ------ https://chatgpt.com/codex/tasks/task_e_686ed0a11314832096a2c9d827d6effa

## Topic 19: HTTP Payload Caching (20 PRs, 1.6%)

**Topic Number:** 19
**Topic Name:** HTTP Payload Caching
**Topic Definition:** Pull requests that tune HTTP payload caching, including cache keys, headers, and storage strategies to reduce repeated downloads.
**Number of PRs in this topic:** 20 (1.6% of all performance PRs)
**Examples:**
1. **PR ID:** 1179
   - **Title:** Cache hub_client.beta.threads.messages.list in environment.py
   - **Description summary:** The `hub_client.beta.threads.messages.list` API call was taking a long time to run and being called repeatedly during agent execution, causing performance issues. This PR implements a message cache in the `Environment` class that: - **Caches messages on first call**: The first...
1. **PR ID:** 64
   - **Title:** [WIP] CachedVariable for ChildSelectors
   - **Description summary:** Thanks for assigning this issue to me. I'm starting to work on it and will keep this PR's description up to date as I form a plan and make progress. Original issue description: > • Add CachedVariable (name pending) property...

## Topic 20: Compiler improvement for Output (20 PRs, 1.6%)

**Topic Number:** 20
**Topic Name:** Compiler improvement for Output
**Topic Definition:** Pull requests that improve the structure or efficiency of compiler output, generating code that runs faster or uses fewer resources.
**Number of PRs in this topic:** 20 (1.6% of all performance PRs)
**Examples:**
1. **PR ID:** 10505
   - **Title:** Improve Lua transpiler
   - **Description summary:** ## Summary - inline builtin operations in Lua emitter - remove helper tracking flags - update Lua tasks checklist - refresh several Lua golden files ## Testing - `go build -tags slow ./transpiler/x/lua` - `go test -tags slow ./transpiler/x/lua -run...
1. **PR ID:** 13026
   - **Title:** Add Lua benchmarks for Rosetta tasks 46-55 and streamline helpers
   - **Description summary:** ## Summary - generate benchmark output for Rosetta programs 46-55 - update Lua ROSETTA progress table with timings - include benchmark output files in repo - refactor Lua transpiler so helper functions are only emitted when referenced ## Testing -...

## Topic 21: Group-by in Compiler (19 PRs, 1.6%)

**Topic Number:** 21
**Topic Name:** Group-by in Compiler
**Topic Definition:** Pull requests that optimize group-by operations in compilers or query engines, improving performance for aggregations.
**Number of PRs in this topic:** 19 (1.6% of all performance PRs)
**Examples:**
1. **PR ID:** 3947
   - **Title:** Optimize vm grouping
   - **Description summary:** ## Summary - optimize group by by precalculating count - regenerate IR golden files ## Testing - `go test ./...` - `go test -tags slow ./tests/vm -run TestVM_IR -update` ------ https://chatgpt.com/codex/tasks/task_e_6861129b9b388320b583fadf63b24343
1. **PR ID:** 3980
   - **Title:** Optimize group by compilation
   - **Description summary:** ## Summary - optimize VM compiler for group queries by storing group index separately - regenerate IR golden files ## Testing - `go test -tags slow ./tests/vm -run TestVM_IR -update` ------ https://chatgpt.com/codex/tasks/task_e_68616031fb8083209432cdba77413783

## Topic 22: Caching Control (19 PRs, 1.6%)

**Topic Number:** 22
**Topic Name:** Caching Control
**Topic Definition:** Pull requests that add or refine controls for caches, such as invalidation rules, cache layers, or configuration knobs.
**Number of PRs in this topic:** 19 (1.6% of all performance PRs)
**Examples:**
1. **PR ID:** 2916
   - **Title:** fix: Prefetch cache grows indefinitely
   - **Description summary:** ## Summary - clean up expired items when prefetching objects so the cache does not grow endlessly ## Testing - `npm test` ------ https://chatgpt.com/codex/tasks/task_e_6878c79b4dd4832db098bcc0c17f5d47
1. **PR ID:** 13639
   - **Title:** Livewrapped Analytics: cleanup analytics cache
   - **Description summary:** robot found a memory leak in the livewrapped auction cache

## Topic 23: Large Workload (19 PRs, 1.6%)

**Topic Number:** 23
**Topic Name:** Large Workload
**Topic Definition:** Pull requests that make the system behave reliably under large or heavy workloads by reducing hotspots and bottlenecks.
**Number of PRs in this topic:** 19 (1.6% of all performance PRs)
**Examples:**
1. **PR ID:** 1253
   - **Title:** Compute point index map lazily
   - **Description summary:** This PR avoids storing `alt->point-idxs` in `alt-table`, instead computing it directly (basically `invert-index`) when needed. This is good because we only actually need this index in one place. Behavior should be unchanged. https://chatgpt.com/codex/tasks/task_e_6844b88d56048331a0349cec4e0720da
1. **PR ID:** 1782
   - **Title:** Add benchmark for deserializing large added vocab +  optimizations
   - **Description summary:** 

## Topic 24: Bundle Size (18 PRs, 1.5%)

**Topic Number:** 24
**Topic Name:** Bundle Size
**Topic Definition:** Pull requests that shrink JavaScript/CSS bundles or split code more effectively, reducing download and parse times for frontends.
**Number of PRs in this topic:** 18 (1.5% of all performance PRs)
**Examples:**
1. **PR ID:** 62558
   - **Title:** [Blazor] Remove sourcemap link comments from production bundles for blazor.web.js and blazor.webassembly.js
   - **Description summary:** This change modifies the Rollup configuration to generate sourcemap files without including sourcemap link comments in production bundles for `blazor.web.js` and `blazor.webassembly.js`. ## Changes Made - Modified `src/Components/Web.JS/rollup.config.mjs` to use `sourcemap: 'hidden'` for production builds of blazor.web.js and blazor.webassembly.js -...
1. **PR ID:** 1633
   - **Title:** Optimize VSCode extension bundle size by adding .js extensions to core imports
   - **Description summary:** This PR optimizes the VSCode extension bundle by converting all core module imports to use explicit `.js` extensions, enabling better tree-shaking and more efficient bundling. ## Changes Made Updated **105 import statements** across **24 TypeScript files** in `packages/vscode/src/` to use...

## Topic 25: Builtin Optimization in Compiler (18 PRs, 1.5%)

**Topic Number:** 25
**Topic Name:** Builtin Optimization in Compiler
**Topic Definition:** Pull requests that optimize built-in compiler intrinsics or runtime functions to make core operations faster.
**Number of PRs in this topic:** 18 (1.5% of all performance PRs)
**Examples:**
1. **PR ID:** 9390
   - **Title:** Improve Zig backend constant folding
   - **Description summary:** ## Summary - optimize `sum` and `avg` when invoked on list literals - regenerate machine output for updated programs - track new Zig programs `fun_three_args` and `sum_builtin` - document progress in TASKS and README ## Testing - `go test ./compiler/x/zig...
1. **PR ID:** 3970
   - **Title:** Add constant folding for more builtins
   - **Description summary:** ## Summary - add compile-time evaluation for count/exists/avg/sum/min/max/values - regenerate IR golden files ## Testing - `go test ./tests/vm -tags slow -run TestVM_IR -update` - `go test ./...` ------ https://chatgpt.com/codex/tasks/task_e_6861503b541c83209690a71f5e732c14

## Topic 26: Kernel Usage Optimzation (17 PRs, 1.4%)

**Topic Number:** 26
**Topic Name:** Kernel Usage Optimzation
**Topic Definition:** Pull requests that optimize low-level kernel or core routines used by many higher-level features, improving overall throughput.
**Number of PRs in this topic:** 17 (1.4% of all performance PRs)
**Examples:**
1. **PR ID:** 79
   - **Title:** Add SIMD optimizations for 23.5% performance improvement
   - **Description summary:** ## Summary This PR implements comprehensive SIMD optimizations for the probe code search engine, addressing the challenge that **BM25 SIMD wasn't providing expected performance gains due to sparse vector characteristics**. Instead of abandoning SIMD, we pivoted to target string processing...
1. **PR ID:** 25061
   - **Title:** [WIP] Improve DFT implementation
   - **Description summary:** ## DFT Implementation Improvements - COMPLETED ### ✅ All Optimizations Implemented and Validated #### 1. **Core Algorithm Optimizations** - [x] **`next_power_of_2` optimization**: 1.87x speedup using bit manipulation - [x] **Threading integration**: 7 parallel execution paths added - [x] **Memory efficiency**:...

## Topic 27: Benchmark Update (17 PRs, 1.4%)

**Topic Number:** 27
**Topic Name:** Benchmark Update
**Topic Definition:** Pull requests that update or extend existing benchmarks so they better represent real workloads or catch regressions earlier.
**Number of PRs in this topic:** 17 (1.4% of all performance PRs)
**Examples:**
1. **PR ID:** 641
   - **Title:** Make benchmarks only run with release builds
   - **Description summary:** This PR enforces that benchmarks can only be run with release builds, preventing execution with debug builds which would provide inconsistent and misleading performance data. ## Changes Made ### 1. Updated Justfile Commands - Removed `target` parameter from `bench` and...
1. **PR ID:** 4150
   - **Title:** Update benchmarks
   - **Description summary:** ## Summary - rerun benchmarks via `make bench` - update `bench/out` files - refresh `BENCHMARK.md` ## Testing - `go test ./...` ------ https://chatgpt.com/codex/tasks/task_e_686252cb92a08320b525a10e7b7ebbd7

## Topic 28: Responsive UI (16 PRs, 1.3%)

**Topic Number:** 28
**Topic Name:** Responsive UI
**Topic Definition:** Pull requests that improve responsiveness of UIs, including frame rate, interaction latency, and perceived smoothness.
**Number of PRs in this topic:** 16 (1.3% of all performance PRs)
**Examples:**
1. **PR ID:** 251153
   - **Title:** Fix notebook sticky scroll flashing by using single reusable delayer
   - **Description summary:** The notebook sticky scroll was experiencing continuous flashing when scrolling headers close to the sticky scroll area. This was caused by improper debouncing in the scroll event handler. ## Root Cause Each scroll event created a new `Delayer(100)` instance, but...
1. **PR ID:** 252342
   - **Title:** Fix sticky scroll performance issue by using correct array for min content width calculation
   - **Description summary:** Sticky scrolling was causing noticeable performance issues and stuttering during scroll operations due to inefficient DOM queries in the `StickyScrollWidget._renderRootNode` method. ## Problem The `_renderRootNode` method was calculating `_minContentWidthInPx` using the old `this._renderedStickyLines` array instead of the newly built `renderedStickyLines`...

## Topic 29: Query Execution (16 PRs, 1.3%)

**Topic Number:** 29
**Topic Name:** Query Execution
**Topic Definition:** Pull requests that optimize execution of complex queries, improving latency, throughput, or resource use.
**Number of PRs in this topic:** 16 (1.3% of all performance PRs)
**Examples:**
1. **PR ID:** 6060
   - **Title:** Replace LINQ Any+Single patterns with Where+FirstOrDefault for better performance
   - **Description summary:** This PR addresses a performance optimization opportunity identified in PR #5717 where the pattern of using `Any()` followed by `Single()` with the same predicate can be improved. ## Problem The existing code uses this pattern in multiple places: ```csharp if...
1. **PR ID:** 21192
   - **Title:** perf: Optimize team bookings query by using batch version
   - **Description summary:** # Optimize Team Bookings Query by Using Batch Version ## What's being changed and why This PR addresses a database performance issue by updating two locations in the web app code that were still using the single-user version of `BookingRepository.getAllAcceptedTeamBookingsOfUser`...

## Topic 30: File Scanning for UI (16 PRs, 1.3%)

**Topic Number:** 30
**Topic Name:** File Scanning for UI
**Topic Definition:** Pull requests that accelerate file scanning or indexing logic that underpins UI features like search or navigation.
**Number of PRs in this topic:** 16 (1.3% of all performance PRs)
**Examples:**
1. **PR ID:** 61
   - **Title:** Add database caching for folder scan results to improve performance
   - **Description summary:** ## 功能概述 / Feature Overview 实现了第一次扫描文件夹后创建数据库，以后再次扫描优先读取数据库，有任何变化都写入数据库的功能。 Implemented database caching functionality where the first folder scan creates a database, subsequent scans prioritize reading from the database, and any changes are written back to the database. ## 主要改动 / Key Changes ###...
1. **PR ID:** 240
   - **Title:** Refactor scanning API to stream files
   - **Description summary:** ## Summary - expose streaming APIs in `ScannerRepositoryInterface` - use `Flow` in `ScannerRepositoryImpl` for file and folder scanning - update use cases to emit items incrementally - adapt `CleanOperationHandler` and `ScannerViewModel` to process new streams ## Testing - `./gradlew tasks...

## Topic 31: HTTP Client (16 PRs, 1.3%)

**Topic Number:** 31
**Topic Name:** HTTP Client
**Topic Definition:** Pull requests that improve HTTP client behavior and performance, such as connection reuse, retries, or streaming.
**Number of PRs in this topic:** 16 (1.3% of all performance PRs)
**Examples:**
1. **PR ID:** 42
   - **Title:** Fix: Remove unnecessary async declarations from synchronous methods
   - **Description summary:** ## Summary - Removed unnecessary `async` declarations from all manager methods that don't contain any `await` statements - Fixed test fixture to not await the now-synchronous `cleanup()` method - Improved code clarity by accurately representing the synchronous nature of Meilisearch...
1. **PR ID:** 3648
   - **Title:** Implement HTTP connection pooling for WxPayServiceApacheHttpImpl
   - **Description summary:** This PR implements HTTP connection pooling for `WxPayServiceApacheHttpImpl` to address performance issues caused by creating new HttpClient instances for each request. ## Problem The current implementation creates a new `HttpClient` for every HTTP request: ```java HttpClientBuilder httpClientBuilder = this.createHttpClientBuilder(useKey); try...

## Topic 32: DTO (15 PRs, 1.2%)

**Topic Number:** 32
**Topic Name:** DTO
**Topic Definition:** Pull requests that refine data transfer objects (DTOs) to reduce over-fetching, serialization cost, or payload size.
**Number of PRs in this topic:** 15 (1.2% of all performance PRs)
**Examples:**
1. **PR ID:** 14069
   - **Title:** Speed up fast retail autocomplete
   - **Description summary:** ## Summary - add `StockDTO` for lighter stock queries - autocomplete uses `StockDTO` results - assign selected stock using DTO id ## Testing - `mvn -q -DskipTests package` *(fails: command not found)* ------ https://chatgpt.com/codex/tasks/task_e_687ee62ebc20832fb7194755a6c2dde2
1. **PR ID:** 14153
   - **Title:** Refactor payment creation for fast retail sales
   - **Description summary:** ## Summary - delegate payment creation to `PaymentProcessingService` ## Testing - `mvn clean compile` *(fails: Could not transfer artifact maven-clean-plugin from https://repo.maven.apache.org)* ------ https://chatgpt.com/codex/tasks/task_e_6882a636a6d8832f9138cb33f66ba543

## Topic 33: Hashing (14 PRs, 1.1%)

**Topic Number:** 33
**Topic Name:** Hashing
**Topic Definition:** Pull requests that improve hashing performance or collision behavior for keys, sets, or maps in hot paths.
**Number of PRs in this topic:** 14 (1.1% of all performance PRs)
**Examples:**
1. **PR ID:** 74
   - **Title:** Convert internal Arrays to Vectors for better performance
   - **Description summary:** This PR converts internal Array usage to Vector for improved performance while maintaining backward compatibility. ## Changes 1. Changed internal storage from Array to Vector: - `Vector.<Class>` for `_valueClasses` in `MonoSignal` and `OnceSignal` - `Vector.<Object>` for `_params` in `Slot` -...
1. **PR ID:** 94
   - **Title:** Add BitmapContext extension methods for direct drawing operations
   - **Description summary:** This PR adds extension methods for the `BitmapContext` class that allow users to perform drawing operations directly on a `BitmapContext` instead of having to go through the `WriteableBitmap`. This enables more efficient code when doing multiple drawing operations since the...

## Topic 34: Telemetry and tracing (14 PRs, 1.1%)

**Topic Number:** 34
**Topic Name:** Telemetry and tracing
**Topic Definition:** Pull requests that add or improve telemetry and tracing so performance characteristics can be observed and debugged.
**Number of PRs in this topic:** 14 (1.1% of all performance PRs)
**Examples:**
1. **PR ID:** 834
   - **Title:** feat: implement async notification and telemetry system (Phase 1-3)
   - **Description summary:** ## Summary This PR implements the first three phases of the async notification and telemetry system as outlined in #833. It introduces a non-blocking event bus architecture that decouples error reporting from notification/telemetry processing, preventing any blocking operations during error...
1. **PR ID:** 841
   - **Title:** feat(telemetry): implement performance testing framework (Phase 8)
   - **Description summary:** ## Summary This PR implements Phase 8 of the telemetry system migration (#833), focusing on comprehensive performance testing and validation. The primary goal was to ensure the telemetry system has minimal performance impact when disabled (<100ns) while providing robust testing...

## Topic 35: Offline Asset Caching (14 PRs, 1.1%)

**Topic Number:** 35
**Topic Name:** Offline Asset Caching
**Topic Definition:** Pull requests that cache static or offline assets more effectively, improving load times and resiliency when offline or on slow networks.
**Number of PRs in this topic:** 14 (1.1% of all performance PRs)
**Examples:**
1. **PR ID:** 4355
   - **Title:** [Failed] Unable to enable browser notifications immediately after visiting the web page for the first time
   - **Description summary:** Thanks for assigning this issue to me. I'm starting to work on it and will keep this PR's description up to date as I form a plan and make progress. Original issue description: > ### Share your bug report, feature...
1. **PR ID:** 1459
   - **Title:** [alpha_factory] add i18n precache
   - **Description summary:** ## Summary - cache locale JSON files in the Insight demo service worker - update build scripts and offline test ## Testing - `python check_env.py --auto-install` - `pytest -q` *(fails: ValueError: Duplicated timeseries in CollectorRegistry)* - `pre-commit run --files alpha_factory_v1/demos/alpha_agi_insight_v1/insight_browser_v1/sw.js...

## Topic 36: N+1 Query Optimization (13 PRs, 1.1%)

**Topic Number:** 36
**Topic Name:** N+1 Query Optimization
**Topic Definition:** Pull requests that eliminate or mitigate N+1 query patterns, often by batching or prefetching related data.
**Number of PRs in this topic:** 13 (1.1% of all performance PRs)
**Examples:**
1. **PR ID:** 252166
   - **Title:** Fix infinite loop caused by empty regex in minimap section header detection
   - **Description summary:** This PR fixes a critical performance issue where setting `editor.minimap.markSectionHeaderRegex` to an empty string causes 100% CPU usage due to an infinite loop in the `collectMarkHeaders` function. ## Problem When users set `editor.minimap.markSectionHeaderRegex` to an empty string (e.g., to disable...
1. **PR ID:** 16039
   - **Title:** Improve `dev/update_changelog.py` performance by batch-fetching PRs with GraphQL API
   - **Description summary:** - [x] Analyze current implementation of `dev/update_changelog.py` - [x] Understand the performance issue: currently fetches PRs one by one with REST API calls - [x] Explore existing codebase for GraphQL usage patterns - [x] Design GraphQL query to batch-fetch PR...

## Topic 37: Rate Limiting (13 PRs, 1.1%)

**Topic Number:** 37
**Topic Name:** Rate Limiting
**Topic Definition:** Pull requests that implement or tune rate limiting to protect services from overload while maintaining good throughput.
**Number of PRs in this topic:** 13 (1.1% of all performance PRs)
**Examples:**
1. **PR ID:** 34529
   - **Title:** Fix file save blocking on entry refresh for improved hot reload performance
   - **Description summary:** ## Summary Fixes file save operations blocking on filesystem entry refresh, which was causing hot reload systems to detect file changes later than other editors like VS Code or Sublime Text. ## Changes Modified `LocalWorktree::write_file` in `crates/worktree/src/worktree.rs` to make the...
1. **PR ID:** 1636
   - **Title:** Implement retry-after header handling for improved throttling in fetch requests
   - **Description summary:** Currently, genaiscript handles throttling situations but does not respect the `retry-after` header returned by services. This leads to unnecessary load on throttled services and suboptimal user experience with exponential backoff delays that may be longer than needed. ## Changes Made...

## Topic 38: .NET build (13 PRs, 1.1%)

**Topic Number:** 38
**Topic Name:** .NET build
**Topic Definition:** Pull requests that specifically improve .NET build performance, including MSBuild, restore, and related tooling.
**Number of PRs in this topic:** 13 (1.1% of all performance PRs)
**Examples:**
1. **PR ID:** 49424
   - **Title:** Add EnableDefaultItems=false optimization for restore operations
   - **Description summary:** Improves restore performance by disabling default item globbing during restore operations, addressing significant performance issues on projects with large numbers of files. ## Problem During `dotnet restore` operations, MSBuild spends excessive time on default item globbing (Compile, EmbeddedResource, None items)...
1. **PR ID:** 12025
   - **Title:** Add fast-paths for ToolLocationHelper property functions
   - **Description summary:** This PR adds fast-path implementations for two commonly used ToolLocationHelper property functions that were identified as performance bottlenecks in template projects: - `GetPlatformSDKLocation(String, String)` - `GetPlatformSDKDisplayName(String, String)` ## Problem When building template projects in .NET 10.0.100-preview.5, these property functions don't...

## Topic 39: Traspiler Improvement for Output (13 PRs, 1.1%)

**Topic Number:** 39
**Topic Name:** Traspiler Improvement for Output
**Topic Definition:** Pull requests that improve transpiler output quality or speed, especially around hot or performance-critical constructs.
**Number of PRs in this topic:** 13 (1.1% of all performance PRs)
**Examples:**
1. **PR ID:** 10824
   - **Title:** Improve TS transpiler join code
   - **Description summary:** ## Summary - inline join loops in ts transpiler - update golden outputs and progress ## Testing - `go test ./transpiler/x/ts -run TestTSTranspiler_VMValid_Golden -count=1 -tags=slow` ------ https://chatgpt.com/codex/tasks/task_e_687cee5d80348320bf4696f31f0d38bd
1. **PR ID:** 10525
   - **Title:** Improve TS transpiler output
   - **Description summary:** ## Summary - improve TypeScript transpiler by omitting `any` type annotations - regenerate affected golden outputs - update task progress log ## Testing - `go test -tags slow ./transpiler/x/ts -run TestMain -count=1` ------ https://chatgpt.com/codex/tasks/task_e_687c641606ac832096e314dfd1d7834d

## Topic 40: Test Timeout (13 PRs, 1.1%)

**Topic Number:** 40
**Topic Name:** Test Timeout
**Topic Definition:** Pull requests that adjust or fix test timeouts so test suites finish faster and avoid unnecessary waiting.
**Number of PRs in this topic:** 13 (1.1% of all performance PRs)
**Examples:**
1. **PR ID:** 4407
   - **Title:** Fix Python test timeouts in full matrix CI workflow
   - **Description summary:** ## Problem Python tests were timing out in the full matrix CI workflow, causing build failures. The issue occurred because: 1. **Full matrix mode runs tests with both async backends sequentially** - Tests run with both `--async-backend=asyncio` and `--async-backend=trio`, effectively...
1. **PR ID:** 4290
   - **Title:** Fix flaky test_cluster_scan_non_covered_slots by replacing inefficient loop with mset
   - **Description summary:** The test `test_cluster_scan_non_covered_slots` was failing intermittently with timeout errors due to an inefficient approach to setting up test data. The test was using a loop to perform 1000 individual `set` operations, which caused performance issues and timeout failures under load....

## Topic 41: Redundant UI Update (12 PRs, 1.0%)

**Topic Number:** 41
**Topic Name:** Redundant UI Update
**Topic Definition:** Pull requests that remove redundant or unnecessary UI updates to avoid wasted rendering and event handling.
**Number of PRs in this topic:** 12 (1.0% of all performance PRs)
**Examples:**
1. **PR ID:** 40
   - **Title:** Fix Claude animation flickering with vt10x-inspired terminal state deduplication
   - **Description summary:** ## 🎯 Problem: Claude's Thinking Animation Causes Terminal Flickering When using Claude in the terminal, rapid escape sequences during the "thinking" animation cause visual chaos: - Cursor jumps left-right-left-right 🔄 - Bottom lines flicker aggressively ⚡ - Text appears and...
1. **PR ID:** 1164
   - **Title:** Fix startup errors and implement real-time Effect streaming
   - **Description summary:** ## Summary Fixes the "Session not found" error on app startup and implements real-time Effect-based streaming to replace 50ms polling. ## Key Changes ### 1. Fix "Session not found" Error - **Problem**: App showed "Session not found" dialog on every...

## Topic 42: VM Register (12 PRs, 1.0%)

**Topic Number:** 42
**Topic Name:** VM Register
**Topic Definition:** Pull requests that optimize VM register usage, such as allocation, layout, or register-based instructions.
**Number of PRs in this topic:** 12 (1.0% of all performance PRs)
**Examples:**
1. **PR ID:** 146
   - **Title:** Improve putAll efficiency
   - **Description summary:** ## Summary - detect large bulk inserts in CompactMap.putAll - copy existing entries directly to a backing map - add regression tests ensuring putAll switches representation when exceeding the threshold ## Testing - `mvn -q test` *(fails: `mvn: command not...
1. **PR ID:** 3563
   - **Title:** Add liveness analysis to VM compiler
   - **Description summary:** ## Summary - add liveness analysis pass for VM functions - track register usage and eliminate dead writes - shrink function register counts after optimization ## Testing - `go test ./runtime/vm -run .` - `go test ./...` *(fails: requires apt...

## Topic 43: .NET micro-optimizations (12 PRs, 1.0%)

**Topic Number:** 43
**Topic Name:** .NET micro-optimizations
**Topic Definition:** Pull requests that make small, targeted performance improvements in .NET code, such as micro-optimizing loops or allocations.
**Number of PRs in this topic:** 12 (1.0% of all performance PRs)
**Examples:**
1. **PR ID:** 47134
   - **Title:** Improve `in` parameter modifier example with meaningful struct-based demonstration
   - **Description summary:** Fixes #25422 ## Problem The current example for the `in` parameter modifier uses a simple `int` parameter, which doesn't effectively demonstrate the purpose and benefits of the `in` modifier. As pointed out in the issue: - Without the `in` keyword,...
1. **PR ID:** 60
   - **Title:** Share static empty metadata
   - **Description summary:** ## Summary - reuse `EmptyMetaData` for `Error.Empty` and `DefaultErrorList` to reduce allocations ## Testing - `dotnet test tests/LightResults.Tests/LightResults.Tests.csproj -f net9.0` ------ https://chatgpt.com/codex/tasks/task_e_686d7f9f169c8328892add17a8fe4897

## Topic 44: GPU Usage (11 PRs, 0.9%)

**Topic Number:** 44
**Topic Name:** GPU Usage
**Topic Definition:** Pull requests that improve how GPU resources are used, for example rendering pipelines or compute workloads.
**Number of PRs in this topic:** 11 (0.9% of all performance PRs)
**Examples:**
1. **PR ID:** 5425
   - **Title:** Add ESLint rule for slow CSS properties that may impact GPU rendering
   - **Description summary:** This PR adds a new ESLint rule `@remotion/slow-css-property` that warns developers when they use CSS properties that may slow down rendering on machines without a GPU. ## What it does The rule detects usage of the following CSS properties in...
1. **PR ID:** 496
   - **Title:** Implement MeshData API and Job System optimization for UMA mesh combiners
   - **Description summary:** This PR implements high-performance mesh combiners that leverage Unity's newer MeshData API and Job System to significantly improve the performance of UMA's mesh combining operations. ## Performance Improvements The new optimized combiners provide substantial performance gains: - **Large meshes** (5000+...

## Topic 45: Caching Expiry (11 PRs, 0.9%)

**Topic Number:** 45
**Topic Name:** Caching Expiry
**Topic Definition:** Pull requests that tune when and how cached entries expire so caches remain efficient and correct.
**Number of PRs in this topic:** 11 (0.9% of all performance PRs)
**Examples:**
1. **PR ID:** 583
   - **Title:** Cache CloudInfo / CloudSettings by authority
   - **Description summary:** This PR modifies `CloudSettings` to cache cloud information by authority (schema, host, and port) rather than by the full URL. This ensures that multiple URLs pointing to the same cluster with different paths will share the same cached `CloudInfo` object....
1. **PR ID:** 9
   - **Title:** Add FastMCP server
   - **Description summary:** ## Summary - add `run_fastmcp.py` for running DeepSearchAgents via FastMCP - document running the new MCP server in README ## Testing - `make test` *(fails: No route to host)*

## Topic 46: Scheduling (11 PRs, 0.9%)

**Topic Number:** 46
**Topic Name:** Scheduling
**Topic Definition:** Pull requests that improve scheduling of background work, jobs, or tasks to balance latency, fairness, and utilization.
**Number of PRs in this topic:** 11 (0.9% of all performance PRs)
**Examples:**
1. **PR ID:** 146
   - **Title:** [WIP] Optimize Placement object with cached computations and Copy-on-Write pattern
   - **Description summary:** - [x] Analyze current Placement implementation in src/ada/api/transforms.py - [x] Examine existing caching in src/ada/geom/placement.py - [x] Identify performance bottlenecks in __post_init__ method - [x] Review existing test structure in tests/core/api/test_placements.py - [ ] Implement immutable PlacementTemplate class for caching...
1. **PR ID:** 7034
   - **Title:** Fix cleanup in network status hook
   - **Description summary:** ## Summary - avoid accumulating event listeners in `useNetworkStatus`

## Topic 47: Go Compiler (11 PRs, 0.9%)

**Topic Number:** 47
**Topic Name:** Go Compiler
**Topic Definition:** Pull requests that optimize Go compiler behavior or generated Go code for performance.
**Number of PRs in this topic:** 11 (0.9% of all performance PRs)
**Examples:**
1. **PR ID:** 1242
   - **Title:** Fix list literal type inference in Go compiler
   - **Description summary:** ## Summary - keep argument type when a list literal is compiled with a type hint - this prevents unnecessary slice conversions ## Testing - `go test ./...` - `make -C examples/leetcode run-go ID=23` ------ https://chatgpt.com/codex/tasks/task_e_6850ef5650588320a1841f4070ac1380
1. **PR ID:** 2758
   - **Title:** Add CFG inference to VM
   - **Description summary:** ## Summary - add a new `infer.go` implementing type inference across the bytecode CFG - rewrite arithmetic/comparison ops based on inferred register types - run the inference optimisation step after compilation - update golden IR outputs for optimised opcodes ##...

## Topic 48: Chat API (10 PRs, 0.8%)

**Topic Number:** 48
**Topic Name:** Chat API
**Topic Definition:** Pull requests that improve the performance and scalability of chat-related APIs and endpoints.
**Number of PRs in this topic:** 10 (0.8% of all performance PRs)
**Examples:**
1. **PR ID:** 711
   - **Title:** Fix AI chat query execution to only run when chat pane is open
   - **Description summary:** Fixes OPS-1876. ## Problem The `useAiAssistantChat` hook was invoking `queryFn` regardless of whether the AI chat pane is open, leading to unnecessary API calls and potential side effects when the pane is closed. ## Solution Modified `useAiAssistantChat` to read `isAiChatOpened`...
1. **PR ID:** 93
   - **Title:** Fix message ordering in chat API
   - **Description summary:** ## Summary - reorder system state message after user messages to optimize caching ## Testing - `npm run build` - `npm run lint` *(fails: Unexpected any, unused vars)*

## Topic 49: Backend Query Update (10 PRs, 0.8%)

**Topic Number:** 49
**Topic Name:** Backend Query Update
**Topic Definition:** Pull requests that adjust or optimize backend query handling, such as filters, joins, or pagination strategies.
**Number of PRs in this topic:** 10 (0.8% of all performance PRs)
**Examples:**
1. **PR ID:** 5001
   - **Title:** Update hufilter URLs to jsDelivr CDN and add missing EF migration
   - **Description summary:** Updated hufilter filter list URLs from deprecated raw GitHub URLs to the new jsDelivr CDN URLs as requested in [hufilter/hufilter-dev#461](https://github.com/hufilter/hufilter-dev/issues/461). The hufilter maintainers have migrated their repository structure and are now serving filter lists through GitHub Pages with jsDelivr CDN...
1. **PR ID:** 250
   - **Title:** Optimize more layout hooks
   - **Description summary:** ## Summary - cache sidebar badge views in `AWEHPTopBarCTAItemView` - cache alpha subviews in `AWEAwemeDetailNaviBarContainerView` - cache avatar subviews in `AWEPlayInteractionUserAvatarView` - cache button subviews for fullscreen hide in `IESLiveButton` - retain prior cached views in tab bar hooks -...

## Topic 50: Redundant Function Call (10 PRs, 0.8%)

**Topic Number:** 50
**Topic Name:** Redundant Function Call
**Topic Definition:** Pull requests that remove redundant function calls or repeated work in hot paths to reduce CPU usage.
**Number of PRs in this topic:** 10 (0.8% of all performance PRs)
**Examples:**
1. **PR ID:** 125
   - **Title:** Refactor EngineTests to use DataDescription::getCellRef instead of helper methods
   - **Description summary:** This PR refactors the EngineTests to use the more efficient `DataDescription::getCellRef` method instead of the helper methods `IntegrationTestFramework::getCell` and `IntegrationTestFramework::getCellById`. ## Changes Made ### 1. Made getCellRef Public - Moved `DataDescription::getCellRef` from private to public section in `Descriptions.h` - This...
1. **PR ID:** 361
   - **Title:** perf: Remove preemptive deepcopy operations from exported methods
   - **Description summary:** This PR removes preemptive `deepcopy()` operations from exported methods in `ExtendedDataSquare` to significantly improve performance by eliminating unnecessary memory allocations. ## Changes Made ### Performance Optimizations - **Removed deepcopy from exported methods**: `Row()`, `Col()`, `RowRoots()`, `ColRoots()`, and `Flattened()` now return...

## Topic 51: GPU Acceleration (10 PRs, 0.8%)

**Topic Number:** 51
**Topic Name:** GPU Acceleration
**Topic Definition:** Pull requests that leverage GPU acceleration more effectively to speed up heavy computations or graphics.
**Number of PRs in this topic:** 10 (0.8% of all performance PRs)
**Examples:**
1. **PR ID:** 15
   - **Title:** Add interactive chart for gh-pages site with Chart.js and toggle controls
   - **Description summary:** This PR replaces the static chart image on the gh-pages site with a fast, lightweight, and interactive chart using Chart.js. ## 🎯 Key Features Added ### Interactive Chart Controls - **Agent Toggles**: Show/hide data for individual agents (Copilot, Codex, Cursor,...
1. **PR ID:** 1332
   - **Title:** [alpha_factory] optimize in-browser frontier rendering
   - **Description summary:** ## Summary - add canvas layer drawing utilities - support heavy evolution work in a Web Worker - switch to canvas for large populations ## Testing - `python check_env.py --auto-install` - `pytest -q` *(fails: Duplicated timeseries in CollectorRegistry)* ------ https://chatgpt.com/codex/tasks/task_e_683c4f38a8288333bdfbee92f1a3688d
