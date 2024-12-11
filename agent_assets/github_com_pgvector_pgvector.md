URL: https://github.com/pgvector/pgvector
---


You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

{{ message }}

[pgvector](/pgvector)/ **[pgvector](/pgvector/pgvector)** Public

- [Notifications](/login?return_to=%2Fpgvector%2Fpgvector) You must be signed in to change notification settings
- [Fork\\
608](/login?return_to=%2Fpgvector%2Fpgvector)
- [Star\\
12.9k](/login?return_to=%2Fpgvector%2Fpgvector)


Open-source vector similarity search for Postgres


### License

[View license](/pgvector/pgvector/blob/master/LICENSE)

[12.9k\\
stars](/pgvector/pgvector/stargazers) [608\\
forks](/pgvector/pgvector/forks) [Branches](/pgvector/pgvector/branches) [Tags](/pgvector/pgvector/tags) [Activity](/pgvector/pgvector/activity)

[Star](/login?return_to=%2Fpgvector%2Fpgvector)

[Notifications](/login?return_to=%2Fpgvector%2Fpgvector) You must be signed in to change notification settings

# pgvector/pgvector

master

[Branches](/pgvector/pgvector/branches) [Tags](/pgvector/pgvector/tags)

[Go to Branches page](/pgvector/pgvector/branches)[Go to Tags page](/pgvector/pgvector/tags)

Go to file

Code

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| ## Latest commit<br>## History<br>[1,660 Commits](/pgvector/pgvector/commits/master/) |
| [.github/workflows](/pgvector/pgvector/tree/master/.github/workflows "This path skips through empty directories") | [.github/workflows](/pgvector/pgvector/tree/master/.github/workflows "This path skips through empty directories") |  |  |
| [sql](/pgvector/pgvector/tree/master/sql "sql") | [sql](/pgvector/pgvector/tree/master/sql "sql") |  |  |
| [src](/pgvector/pgvector/tree/master/src "src") | [src](/pgvector/pgvector/tree/master/src "src") |  |  |
| [test](/pgvector/pgvector/tree/master/test "test") | [test](/pgvector/pgvector/tree/master/test "test") |  |  |
| [.dockerignore](/pgvector/pgvector/blob/master/.dockerignore ".dockerignore") | [.dockerignore](/pgvector/pgvector/blob/master/.dockerignore ".dockerignore") |  |  |
| [.editorconfig](/pgvector/pgvector/blob/master/.editorconfig ".editorconfig") | [.editorconfig](/pgvector/pgvector/blob/master/.editorconfig ".editorconfig") |  |  |
| [.gitignore](/pgvector/pgvector/blob/master/.gitignore ".gitignore") | [.gitignore](/pgvector/pgvector/blob/master/.gitignore ".gitignore") |  |  |
| [CHANGELOG.md](/pgvector/pgvector/blob/master/CHANGELOG.md "CHANGELOG.md") | [CHANGELOG.md](/pgvector/pgvector/blob/master/CHANGELOG.md "CHANGELOG.md") |  |  |
| [Dockerfile](/pgvector/pgvector/blob/master/Dockerfile "Dockerfile") | [Dockerfile](/pgvector/pgvector/blob/master/Dockerfile "Dockerfile") |  |  |
| [LICENSE](/pgvector/pgvector/blob/master/LICENSE "LICENSE") | [LICENSE](/pgvector/pgvector/blob/master/LICENSE "LICENSE") |  |  |
| [META.json](/pgvector/pgvector/blob/master/META.json "META.json") | [META.json](/pgvector/pgvector/blob/master/META.json "META.json") |  |  |
| [Makefile](/pgvector/pgvector/blob/master/Makefile "Makefile") | [Makefile](/pgvector/pgvector/blob/master/Makefile "Makefile") |  |  |
| [Makefile.win](/pgvector/pgvector/blob/master/Makefile.win "Makefile.win") | [Makefile.win](/pgvector/pgvector/blob/master/Makefile.win "Makefile.win") |  |  |
| [README.md](/pgvector/pgvector/blob/master/README.md "README.md") | [README.md](/pgvector/pgvector/blob/master/README.md "README.md") |  |  |
| [vector.control](/pgvector/pgvector/blob/master/vector.control "vector.control") | [vector.control](/pgvector/pgvector/blob/master/vector.control "vector.control") |  |  |
| View all files |

## Repository files navigation

# pgvector

[Permalink: pgvector](#pgvector)

Open-source vector similarity search for Postgres

Store your vectors with the rest of your data. Supports:

- exact and approximate nearest neighbor search
- single-precision, half-precision, binary, and sparse vectors
- L2 distance, inner product, cosine distance, L1 distance, Hamming distance, and Jaccard distance
- any [language](#languages) with a Postgres client

Plus [ACID](https://en.wikipedia.org/wiki/ACID) compliance, point-in-time recovery, JOINs, and all of the other [great features](https://www.postgresql.org/about/) of Postgres

[![Build Status](https://github.com/pgvector/pgvector/actions/workflows/build.yml/badge.svg)](https://github.com/pgvector/pgvector/actions)

## Installation

[Permalink: Installation](#installation)

### Linux and Mac

[Permalink: Linux and Mac](#linux-and-mac)

Compile and install the extension (supports Postgres 13+)

```
cd /tmp
git clone --branch v0.8.0 https://github.com/pgvector/pgvector.git
cd pgvector
make
make install # may need sudo
```

See the [installation notes](#installation-notes---linux-and-mac) if you run into issues

You can also install it with [Docker](#docker), [Homebrew](#homebrew), [PGXN](#pgxn), [APT](#apt), [Yum](#yum), [pkg](#pkg), or [conda-forge](#conda-forge), and it comes preinstalled with [Postgres.app](#postgresapp) and many [hosted providers](#hosted-postgres). There are also instructions for [GitHub Actions](https://github.com/pgvector/setup-pgvector).

### Windows

[Permalink: Windows](#windows)

Ensure [C++ support in Visual Studio](https://learn.microsoft.com/en-us/cpp/build/building-on-the-command-line?view=msvc-170#download-and-install-the-tools) is installed, and run:

```
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
```

Note: The exact path will vary depending on your Visual Studio version and edition

Then use `nmake` to build:

```
set "PGROOT=C:\Program Files\PostgreSQL\16"
cd %TEMP%
git clone --branch v0.8.0 https://github.com/pgvector/pgvector.git
cd pgvector
nmake /F Makefile.win
nmake /F Makefile.win install
```

Note: Postgres 17 is not supported with MSVC yet due to an [upstream issue](https://www.postgresql.org/message-id/flat/CAOdR5yF0krWrxycA04rgUKCgKugRvGWzzGLAhDZ9bzNv8g0Lag%40mail.gmail.com)

See the [installation notes](#installation-notes---windows) if you run into issues

You can also install it with [Docker](#docker) or [conda-forge](#conda-forge).

## Getting Started

[Permalink: Getting Started](#getting-started)

Enable the extension (do this once in each database where you want to use it)

```
CREATE EXTENSION vector;
```

Create a vector column with 3 dimensions

```
CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(3));
```

Insert vectors

```
INSERT INTO items (embedding) VALUES ('[1,2,3]'), ('[4,5,6]');
```

Get the nearest neighbors by L2 distance

```
SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

Also supports inner product ( `<#>`), cosine distance ( `<=>`), and L1 distance ( `<+>`, added in 0.7.0)

Note: `<#>` returns the negative inner product since Postgres only supports `ASC` order index scans on operators

## Storing

[Permalink: Storing](#storing)

Create a new table with a vector column

```
CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(3));
```

Or add a vector column to an existing table

```
ALTER TABLE items ADD COLUMN embedding vector(3);
```

Also supports [half-precision](#half-precision-vectors), [binary](#binary-vectors), and [sparse](#sparse-vectors) vectors

Insert vectors

```
INSERT INTO items (embedding) VALUES ('[1,2,3]'), ('[4,5,6]');
```

Or load vectors in bulk using `COPY` ( [example](https://github.com/pgvector/pgvector-python/blob/master/examples/loading/example.py))

```
COPY items (embedding) FROM STDIN WITH (FORMAT BINARY);
```

Upsert vectors

```
INSERT INTO items (id, embedding) VALUES (1, '[1,2,3]'), (2, '[4,5,6]')
    ON CONFLICT (id) DO UPDATE SET embedding = EXCLUDED.embedding;
```

Update vectors

```
UPDATE items SET embedding = '[1,2,3]' WHERE id = 1;
```

Delete vectors

```
DELETE FROM items WHERE id = 1;
```

## Querying

[Permalink: Querying](#querying)

Get the nearest neighbors to a vector

```
SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

Supported distance functions are:

- `<->` \- L2 distance
- `<#>` \- (negative) inner product
- `<=>` \- cosine distance
- `<+>` \- L1 distance (added in 0.7.0)
- `<~>` \- Hamming distance (binary vectors, added in 0.7.0)
- `<%>` \- Jaccard distance (binary vectors, added in 0.7.0)

Get the nearest neighbors to a row

```
SELECT * FROM items WHERE id != 1 ORDER BY embedding <-> (SELECT embedding FROM items WHERE id = 1) LIMIT 5;
```

Get rows within a certain distance

```
SELECT * FROM items WHERE embedding <-> '[3,1,2]' < 5;
```

Note: Combine with `ORDER BY` and `LIMIT` to use an index

#### Distances

[Permalink: Distances](#distances)

Get the distance

```
SELECT embedding <-> '[3,1,2]' AS distance FROM items;
```

For inner product, multiply by -1 (since `<#>` returns the negative inner product)

```
SELECT (embedding <#> '[3,1,2]') * -1 AS inner_product FROM items;
```

For cosine similarity, use 1 - cosine distance

```
SELECT 1 - (embedding <=> '[3,1,2]') AS cosine_similarity FROM items;
```

#### Aggregates

[Permalink: Aggregates](#aggregates)

Average vectors

```
SELECT AVG(embedding) FROM items;
```

Average groups of vectors

```
SELECT category_id, AVG(embedding) FROM items GROUP BY category_id;
```

## Indexing

[Permalink: Indexing](#indexing)

By default, pgvector performs exact nearest neighbor search, which provides perfect recall.

You can add an index to use approximate nearest neighbor search, which trades some recall for speed. Unlike typical indexes, you will see different results for queries after adding an approximate index.

Supported index types are:

- [HNSW](#hnsw)
- [IVFFlat](#ivfflat)

## HNSW

[Permalink: HNSW](#hnsw)

An HNSW index creates a multilayer graph. It has better query performance than IVFFlat (in terms of speed-recall tradeoff), but has slower build times and uses more memory. Also, an index can be created without any data in the table since there isn’t a training step like IVFFlat.

Add an index for each distance function you want to use.

L2 distance

```
CREATE INDEX ON items USING hnsw (embedding vector_l2_ops);
```

Note: Use `halfvec_l2_ops` for `halfvec` and `sparsevec_l2_ops` for `sparsevec` (and similar with the other distance functions)

Inner product

```
CREATE INDEX ON items USING hnsw (embedding vector_ip_ops);
```

Cosine distance

```
CREATE INDEX ON items USING hnsw (embedding vector_cosine_ops);
```

L1 distance - added in 0.7.0

```
CREATE INDEX ON items USING hnsw (embedding vector_l1_ops);
```

Hamming distance - added in 0.7.0

```
CREATE INDEX ON items USING hnsw (embedding bit_hamming_ops);
```

Jaccard distance - added in 0.7.0

```
CREATE INDEX ON items USING hnsw (embedding bit_jaccard_ops);
```

Supported types are:

- `vector` \- up to 2,000 dimensions
- `halfvec` \- up to 4,000 dimensions (added in 0.7.0)
- `bit` \- up to 64,000 dimensions (added in 0.7.0)
- `sparsevec` \- up to 1,000 non-zero elements (added in 0.7.0)

### Index Options

[Permalink: Index Options](#index-options)

Specify HNSW parameters

- `m` \- the max number of connections per layer (16 by default)
- `ef_construction` \- the size of the dynamic candidate list for constructing the graph (64 by default)

```
CREATE INDEX ON items USING hnsw (embedding vector_l2_ops) WITH (m = 16, ef_construction = 64);
```

A higher value of `ef_construction` provides better recall at the cost of index build time / insert speed.

### Query Options

[Permalink: Query Options](#query-options)

Specify the size of the dynamic candidate list for search (40 by default)

```
SET hnsw.ef_search = 100;
```

A higher value provides better recall at the cost of speed.

Use `SET LOCAL` inside a transaction to set it for a single query

```
BEGIN;
SET LOCAL hnsw.ef_search = 100;
SELECT ...
COMMIT;
```

### Index Build Time

[Permalink: Index Build Time](#index-build-time)

Indexes build significantly faster when the graph fits into `maintenance_work_mem`

```
SET maintenance_work_mem = '8GB';
```

A notice is shown when the graph no longer fits

```
NOTICE:  hnsw graph no longer fits into maintenance_work_mem after 100000 tuples
DETAIL:  Building will take significantly more time.
HINT:  Increase maintenance_work_mem to speed up builds.

```

Note: Do not set `maintenance_work_mem` so high that it exhausts the memory on the server

Like other index types, it’s faster to create an index after loading your initial data

Starting with 0.6.0, you can also speed up index creation by increasing the number of parallel workers (2 by default)

```
SET max_parallel_maintenance_workers = 7; -- plus leader
```

For a large number of workers, you may also need to increase `max_parallel_workers` (8 by default)

### Indexing Progress

[Permalink: Indexing Progress](#indexing-progress)

Check [indexing progress](https://www.postgresql.org/docs/current/progress-reporting.html#CREATE-INDEX-PROGRESS-REPORTING)

```
SELECT phase, round(100.0 * blocks_done / nullif(blocks_total, 0), 1) AS "%" FROM pg_stat_progress_create_index;
```

The phases for HNSW are:

1. `initializing`
2. `loading tuples`

## IVFFlat

[Permalink: IVFFlat](#ivfflat)

An IVFFlat index divides vectors into lists, and then searches a subset of those lists that are closest to the query vector. It has faster build times and uses less memory than HNSW, but has lower query performance (in terms of speed-recall tradeoff).

Three keys to achieving good recall are:

1. Create the index _after_ the table has some data
2. Choose an appropriate number of lists - a good place to start is `rows / 1000` for up to 1M rows and `sqrt(rows)` for over 1M rows
3. When querying, specify an appropriate number of [probes](#query-options) (higher is better for recall, lower is better for speed) - a good place to start is `sqrt(lists)`

Add an index for each distance function you want to use.

L2 distance

```
CREATE INDEX ON items USING ivfflat (embedding vector_l2_ops) WITH (lists = 100);
```

Note: Use `halfvec_l2_ops` for `halfvec` (and similar with the other distance functions)

Inner product

```
CREATE INDEX ON items USING ivfflat (embedding vector_ip_ops) WITH (lists = 100);
```

Cosine distance

```
CREATE INDEX ON items USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
```

Hamming distance - added in 0.7.0

```
CREATE INDEX ON items USING ivfflat (embedding bit_hamming_ops) WITH (lists = 100);
```

Supported types are:

- `vector` \- up to 2,000 dimensions
- `halfvec` \- up to 4,000 dimensions (added in 0.7.0)
- `bit` \- up to 64,000 dimensions (added in 0.7.0)

### Query Options

[Permalink: Query Options](#query-options-1)

Specify the number of probes (1 by default)

```
SET ivfflat.probes = 10;
```

A higher value provides better recall at the cost of speed, and it can be set to the number of lists for exact nearest neighbor search (at which point the planner won’t use the index)

Use `SET LOCAL` inside a transaction to set it for a single query

```
BEGIN;
SET LOCAL ivfflat.probes = 10;
SELECT ...
COMMIT;
```

### Index Build Time

[Permalink: Index Build Time](#index-build-time-1)

Speed up index creation on large tables by increasing the number of parallel workers (2 by default)

```
SET max_parallel_maintenance_workers = 7; -- plus leader
```

For a large number of workers, you may also need to increase `max_parallel_workers` (8 by default)

### Indexing Progress

[Permalink: Indexing Progress](#indexing-progress-1)

Check [indexing progress](https://www.postgresql.org/docs/current/progress-reporting.html#CREATE-INDEX-PROGRESS-REPORTING)

```
SELECT phase, round(100.0 * tuples_done / nullif(tuples_total, 0), 1) AS "%" FROM pg_stat_progress_create_index;
```

The phases for IVFFlat are:

1. `initializing`
2. `performing k-means`
3. `assigning tuples`
4. `loading tuples`

Note: `%` is only populated during the `loading tuples` phase

## Filtering

[Permalink: Filtering](#filtering)

There are a few ways to index nearest neighbor queries with a `WHERE` clause.

```
SELECT * FROM items WHERE category_id = 123 ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

A good place to start is creating an index on the filter column. This can provide fast, exact nearest neighbor search in many cases. Postgres has a number of [index types](https://www.postgresql.org/docs/current/indexes-types.html) for this: B-tree (default), hash, GiST, SP-GiST, GIN, and BRIN.

```
CREATE INDEX ON items (category_id);
```

For multiple columns, consider a [multicolumn index](https://www.postgresql.org/docs/current/indexes-multicolumn.html).

```
CREATE INDEX ON items (location_id, category_id);
```

Exact indexes work well for conditions that match a low percentage of rows. Otherwise, [approximate indexes](#indexing) can work better.

```
CREATE INDEX ON items USING hnsw (embedding vector_l2_ops);
```

With approximate indexes, filtering is applied _after_ the index is scanned. If a condition matches 10% of rows, with HNSW and the default `hnsw.ef_search` of 40, only 4 rows will match on average. For more rows, increase `hnsw.ef_search`.

```
SET hnsw.ef_search = 200;
```

Starting with 0.8.0, you can enable [iterative index scans](#iterative-index-scans), which will automatically scan more of the index when needed.

```
SET hnsw.iterative_scan = strict_order;
```

If filtering by only a few distinct values, consider [partial indexing](https://www.postgresql.org/docs/current/indexes-partial.html).

```
CREATE INDEX ON items USING hnsw (embedding vector_l2_ops) WHERE (category_id = 123);
```

If filtering by many different values, consider [partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html).

```
CREATE TABLE items (embedding vector(3), category_id int) PARTITION BY LIST(category_id);
```

## Iterative Index Scans

[Permalink: Iterative Index Scans](#iterative-index-scans)

_Added in 0.8.0_

With approximate indexes, queries with filtering can return less results since filtering is applied _after_ the index is scanned. Starting with 0.8.0, you can enable iterative index scans, which will automatically scan more of the index until enough results are found (or it reaches `hnsw.max_scan_tuples` or `ivfflat.max_probes`).

Iterative scans can use strict or relaxed ordering.

Strict ensures results are in the exact order by distance

```
SET hnsw.iterative_scan = strict_order;
```

Relaxed allows results to be slightly out of order by distance, but provides better recall

```
SET hnsw.iterative_scan = relaxed_order;
# or
SET ivfflat.iterative_scan = relaxed_order;
```

With relaxed ordering, you can use a [materialized CTE](https://www.postgresql.org/docs/current/queries-with.html#QUERIES-WITH-CTE-MATERIALIZATION) to get strict ordering

```
WITH relaxed_results AS MATERIALIZED (
    SELECT id, embedding <-> '[1,2,3]' AS distance FROM items WHERE category_id = 123 ORDER BY distance LIMIT 5
) SELECT * FROM relaxed_results ORDER BY distance;
```

For queries that filter by distance, use a materialized CTE and place the distance filter outside of it for best performance (due to the [current behavior](https://www.postgresql.org/message-id/flat/CAOdR5yGUoMQ6j7M5hNUXrySzaqZVGf_Ne%2B8fwZMRKTFxU1nbJg%40mail.gmail.com) of the Postgres executor)

```
WITH nearest_results AS MATERIALIZED (
    SELECT id, embedding <-> '[1,2,3]' AS distance FROM items ORDER BY distance LIMIT 5
) SELECT * FROM nearest_results WHERE distance < 5 ORDER BY distance;
```

Note: Place any other filters inside the CTE

### Iterative Scan Options

[Permalink: Iterative Scan Options](#iterative-scan-options)

Since scanning a large portion of an approximate index is expensive, there are options to control when a scan ends.

#### HNSW

[Permalink: HNSW](#hnsw-1)

Specify the max number of tuples to visit (20,000 by default)

```
SET hnsw.max_scan_tuples = 20000;
```

Note: This is approximate and does not affect the initial scan

Specify the max amount of memory to use, as a multiple of `work_mem` (1 by default)

```
SET hnsw.scan_mem_multiplier = 2;
```

Note: Try increasing this if increasing `hnsw.max_scan_tuples` does not improve recall

#### IVFFlat

[Permalink: IVFFlat](#ivfflat-1)

Specify the max number of probes

```
SET ivfflat.max_probes = 100;
```

Note: If this is lower than `ivfflat.probes`, `ivfflat.probes` will be used

## Half-Precision Vectors

[Permalink: Half-Precision Vectors](#half-precision-vectors)

_Added in 0.7.0_

Use the `halfvec` type to store half-precision vectors

```
CREATE TABLE items (id bigserial PRIMARY KEY, embedding halfvec(3));
```

## Half-Precision Indexing

[Permalink: Half-Precision Indexing](#half-precision-indexing)

_Added in 0.7.0_

Index vectors at half precision for smaller indexes

```
CREATE INDEX ON items USING hnsw ((embedding::halfvec(3)) halfvec_l2_ops);
```

Get the nearest neighbors

```
SELECT * FROM items ORDER BY embedding::halfvec(3) <-> '[1,2,3]' LIMIT 5;
```

## Binary Vectors

[Permalink: Binary Vectors](#binary-vectors)

Use the `bit` type to store binary vectors ( [example](https://github.com/pgvector/pgvector-python/blob/master/examples/imagehash/example.py))

```
CREATE TABLE items (id bigserial PRIMARY KEY, embedding bit(3));
INSERT INTO items (embedding) VALUES ('000'), ('111');
```

Get the nearest neighbors by Hamming distance (added in 0.7.0)

```
SELECT * FROM items ORDER BY embedding <~> '101' LIMIT 5;
```

Or (before 0.7.0)

```
SELECT * FROM items ORDER BY bit_count(embedding # '101') LIMIT 5;
```

Also supports Jaccard distance ( `<%>`)

## Binary Quantization

[Permalink: Binary Quantization](#binary-quantization)

_Added in 0.7.0_

Use expression indexing for binary quantization

```
CREATE INDEX ON items USING hnsw ((binary_quantize(embedding)::bit(3)) bit_hamming_ops);
```

Get the nearest neighbors by Hamming distance

```
SELECT * FROM items ORDER BY binary_quantize(embedding)::bit(3) <~> binary_quantize('[1,-2,3]') LIMIT 5;
```

Re-rank by the original vectors for better recall

```
SELECT * FROM (
    SELECT * FROM items ORDER BY binary_quantize(embedding)::bit(3) <~> binary_quantize('[1,-2,3]') LIMIT 20
) ORDER BY embedding <=> '[1,-2,3]' LIMIT 5;
```

## Sparse Vectors

[Permalink: Sparse Vectors](#sparse-vectors)

_Added in 0.7.0_

Use the `sparsevec` type to store sparse vectors

```
CREATE TABLE items (id bigserial PRIMARY KEY, embedding sparsevec(5));
```

Insert vectors

```
INSERT INTO items (embedding) VALUES ('{1:1,3:2,5:3}/5'), ('{1:4,3:5,5:6}/5');
```

The format is `{index1:value1,index2:value2}/dimensions` and indices start at 1 like SQL arrays

Get the nearest neighbors by L2 distance

```
SELECT * FROM items ORDER BY embedding <-> '{1:3,3:1,5:2}/5' LIMIT 5;
```

## Hybrid Search

[Permalink: Hybrid Search](#hybrid-search)

Use together with Postgres [full-text search](https://www.postgresql.org/docs/current/textsearch-intro.html) for hybrid search.

```
SELECT id, content FROM items, plainto_tsquery('hello search') query
    WHERE textsearch @@ query ORDER BY ts_rank_cd(textsearch, query) DESC LIMIT 5;
```

You can use [Reciprocal Rank Fusion](https://github.com/pgvector/pgvector-python/blob/master/examples/hybrid_search/rrf.py) or a [cross-encoder](https://github.com/pgvector/pgvector-python/blob/master/examples/hybrid_search/cross_encoder.py) to combine results.

## Indexing Subvectors

[Permalink: Indexing Subvectors](#indexing-subvectors)

_Added in 0.7.0_

Use expression indexing to index subvectors

```
CREATE INDEX ON items USING hnsw ((subvector(embedding, 1, 3)::vector(3)) vector_cosine_ops);
```

Get the nearest neighbors by cosine distance

```
SELECT * FROM items ORDER BY subvector(embedding, 1, 3)::vector(3) <=> subvector('[1,2,3,4,5]'::vector, 1, 3) LIMIT 5;
```

Re-rank by the full vectors for better recall

```
SELECT * FROM (
    SELECT * FROM items ORDER BY subvector(embedding, 1, 3)::vector(3) <=> subvector('[1,2,3,4,5]'::vector, 1, 3) LIMIT 20
) ORDER BY embedding <=> '[1,2,3,4,5]' LIMIT 5;
```

## Performance

[Permalink: Performance](#performance)

### Tuning

[Permalink: Tuning](#tuning)

Use a tool like [PgTune](https://pgtune.leopard.in.ua/) to set initial values for Postgres server parameters. For instance, `shared_buffers` should typically be 25% of the server’s memory. You can find the config file with:

```
SHOW config_file;
```

And check individual settings with:

```
SHOW shared_buffers;
```

Be sure to restart Postgres for changes to take effect.

### Loading

[Permalink: Loading](#loading)

Use `COPY` for bulk loading data ( [example](https://github.com/pgvector/pgvector-python/blob/master/examples/loading/example.py)).

```
COPY items (embedding) FROM STDIN WITH (FORMAT BINARY);
```

Add any indexes _after_ loading the initial data for best performance.

### Indexing

[Permalink: Indexing](#indexing-1)

See index build time for [HNSW](#index-build-time) and [IVFFlat](#index-build-time-1).

In production environments, create indexes concurrently to avoid blocking writes.

```
CREATE INDEX CONCURRENTLY ...
```

### Querying

[Permalink: Querying](#querying-1)

Use `EXPLAIN ANALYZE` to debug performance.

```
EXPLAIN ANALYZE SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

#### Exact Search

[Permalink: Exact Search](#exact-search)

To speed up queries without an index, increase `max_parallel_workers_per_gather`.

```
SET max_parallel_workers_per_gather = 4;
```

If vectors are normalized to length 1 (like [OpenAI embeddings](https://platform.openai.com/docs/guides/embeddings/which-distance-function-should-i-use)), use inner product for best performance.

```
SELECT * FROM items ORDER BY embedding <#> '[3,1,2]' LIMIT 5;
```

#### Approximate Search

[Permalink: Approximate Search](#approximate-search)

To speed up queries with an IVFFlat index, increase the number of inverted lists (at the expense of recall).

```
CREATE INDEX ON items USING ivfflat (embedding vector_l2_ops) WITH (lists = 1000);
```

### Vacuuming

[Permalink: Vacuuming](#vacuuming)

Vacuuming can take a while for HNSW indexes. Speed it up by reindexing first.

```
REINDEX INDEX CONCURRENTLY index_name;
VACUUM table_name;
```

## Monitoring

[Permalink: Monitoring](#monitoring)

Monitor performance with [pg\_stat\_statements](https://www.postgresql.org/docs/current/pgstatstatements.html) (be sure to add it to `shared_preload_libraries`).

```
CREATE EXTENSION pg_stat_statements;
```

Get the most time-consuming queries with:

```
SELECT query, calls, ROUND((total_plan_time + total_exec_time) / calls) AS avg_time_ms,
    ROUND((total_plan_time + total_exec_time) / 60000) AS total_time_min
    FROM pg_stat_statements ORDER BY total_plan_time + total_exec_time DESC LIMIT 20;
```

Note: Replace `total_plan_time + total_exec_time` with `total_time` for Postgres < 13

Monitor recall by comparing results from approximate search with exact search.

```
BEGIN;
SET LOCAL enable_indexscan = off; -- use exact search
SELECT ...
COMMIT;
```

## Scaling

[Permalink: Scaling](#scaling)

Scale pgvector the same way you scale Postgres.

Scale vertically by increasing memory, CPU, and storage on a single instance. Use existing tools to [tune parameters](#tuning) and [monitor performance](#monitoring).

Scale horizontally with [replicas](https://www.postgresql.org/docs/current/hot-standby.html), or use [Citus](https://github.com/citusdata/citus) or another approach for sharding ( [example](https://github.com/pgvector/pgvector-python/blob/master/examples/citus/example.py)).

## Languages

[Permalink: Languages](#languages)

Use pgvector from any language with a Postgres client. You can even generate and store vectors in one language and query them in another.

| Language | Libraries / Examples |
| --- | --- |
| C | [pgvector-c](https://github.com/pgvector/pgvector-c) |
| C++ | [pgvector-cpp](https://github.com/pgvector/pgvector-cpp) |
| C#, F#, Visual Basic | [pgvector-dotnet](https://github.com/pgvector/pgvector-dotnet) |
| Crystal | [pgvector-crystal](https://github.com/pgvector/pgvector-crystal) |
| D | [pgvector-d](https://github.com/pgvector/pgvector-d) |
| Dart | [pgvector-dart](https://github.com/pgvector/pgvector-dart) |
| Elixir | [pgvector-elixir](https://github.com/pgvector/pgvector-elixir) |
| Erlang | [pgvector-erlang](https://github.com/pgvector/pgvector-erlang) |
| Fortran | [pgvector-fortran](https://github.com/pgvector/pgvector-fortran) |
| Gleam | [pgvector-gleam](https://github.com/pgvector/pgvector-gleam) |
| Go | [pgvector-go](https://github.com/pgvector/pgvector-go) |
| Haskell | [pgvector-haskell](https://github.com/pgvector/pgvector-haskell) |
| Java, Kotlin, Groovy, Scala | [pgvector-java](https://github.com/pgvector/pgvector-java) |
| JavaScript, TypeScript | [pgvector-node](https://github.com/pgvector/pgvector-node) |
| Julia | [pgvector-julia](https://github.com/pgvector/pgvector-julia) |
| Lisp | [pgvector-lisp](https://github.com/pgvector/pgvector-lisp) |
| Lua | [pgvector-lua](https://github.com/pgvector/pgvector-lua) |
| Nim | [pgvector-nim](https://github.com/pgvector/pgvector-nim) |
| OCaml | [pgvector-ocaml](https://github.com/pgvector/pgvector-ocaml) |
| Perl | [pgvector-perl](https://github.com/pgvector/pgvector-perl) |
| PHP | [pgvector-php](https://github.com/pgvector/pgvector-php) |
| Python | [pgvector-python](https://github.com/pgvector/pgvector-python) |
| R | [pgvector-r](https://github.com/pgvector/pgvector-r) |
| Raku | [pgvector-raku](https://github.com/pgvector/pgvector-raku) |
| Ruby | [pgvector-ruby](https://github.com/pgvector/pgvector-ruby), [Neighbor](https://github.com/ankane/neighbor) |
| Rust | [pgvector-rust](https://github.com/pgvector/pgvector-rust) |
| Swift | [pgvector-swift](https://github.com/pgvector/pgvector-swift) |
| Zig | [pgvector-zig](https://github.com/pgvector/pgvector-zig) |

## Frequently Asked Questions

[Permalink: Frequently Asked Questions](#frequently-asked-questions)

#### How many vectors can be stored in a single table?

[Permalink: How many vectors can be stored in a single table?](#how-many-vectors-can-be-stored-in-a-single-table)

A non-partitioned table has a limit of 32 TB by default in Postgres. A partitioned table can have thousands of partitions of that size.

#### Is replication supported?

[Permalink: Is replication supported?](#is-replication-supported)

Yes, pgvector uses the write-ahead log (WAL), which allows for replication and point-in-time recovery.

#### What if I want to index vectors with more than 2,000 dimensions?

[Permalink: What if I want to index vectors with more than 2,000 dimensions?](#what-if-i-want-to-index-vectors-with-more-than-2000-dimensions)

You can use [half-precision indexing](#half-precision-indexing) to index up to 4,000 dimensions or [binary quantization](#binary-quantization) to index up to 64,000 dimensions. Another option is [dimensionality reduction](https://en.wikipedia.org/wiki/Dimensionality_reduction).

#### Can I store vectors with different dimensions in the same column?

[Permalink: Can I store vectors with different dimensions in the same column?](#can-i-store-vectors-with-different-dimensions-in-the-same-column)

You can use `vector` as the type (instead of `vector(3)`).

```
CREATE TABLE embeddings (model_id bigint, item_id bigint, embedding vector, PRIMARY KEY (model_id, item_id));
```

However, you can only create indexes on rows with the same number of dimensions (using [expression](https://www.postgresql.org/docs/current/indexes-expressional.html) and [partial](https://www.postgresql.org/docs/current/indexes-partial.html) indexing):

```
CREATE INDEX ON embeddings USING hnsw ((embedding::vector(3)) vector_l2_ops) WHERE (model_id = 123);
```

and query with:

```
SELECT * FROM embeddings WHERE model_id = 123 ORDER BY embedding::vector(3) <-> '[3,1,2]' LIMIT 5;
```

#### Can I store vectors with more precision?

[Permalink: Can I store vectors with more precision?](#can-i-store-vectors-with-more-precision)

You can use the `double precision[]` or `numeric[]` type to store vectors with more precision.

```
CREATE TABLE items (id bigserial PRIMARY KEY, embedding double precision[]);

-- use {} instead of [] for Postgres arrays
INSERT INTO items (embedding) VALUES ('{1,2,3}'), ('{4,5,6}');
```

Optionally, add a [check constraint](https://www.postgresql.org/docs/current/ddl-constraints.html) to ensure data can be converted to the `vector` type and has the expected dimensions.

```
ALTER TABLE items ADD CHECK (vector_dims(embedding::vector) = 3);
```

Use [expression indexing](https://www.postgresql.org/docs/current/indexes-expressional.html) to index (at a lower precision):

```
CREATE INDEX ON items USING hnsw ((embedding::vector(3)) vector_l2_ops);
```

and query with:

```
SELECT * FROM items ORDER BY embedding::vector(3) <-> '[3,1,2]' LIMIT 5;
```

#### Do indexes need to fit into memory?

[Permalink: Do indexes need to fit into memory?](#do-indexes-need-to-fit-into-memory)

No, but like other index types, you’ll likely see better performance if they do. You can get the size of an index with:

```
SELECT pg_size_pretty(pg_relation_size('index_name'));
```

## Troubleshooting

[Permalink: Troubleshooting](#troubleshooting)

#### Why isn’t a query using an index?

[Permalink: Why isn’t a query using an index?](#why-isnt-a-query-using-an-index)

The query needs to have an `ORDER BY` and `LIMIT`, and the `ORDER BY` must be the result of a distance operator (not an expression) in ascending order.

```
-- index
ORDER BY embedding <=> '[3,1,2]' LIMIT 5;

-- no index
ORDER BY 1 - (embedding <=> '[3,1,2]') DESC LIMIT 5;
```

You can encourage the planner to use an index for a query with:

```
BEGIN;
SET LOCAL enable_seqscan = off;
SELECT ...
COMMIT;
```

Also, if the table is small, a table scan may be faster.

#### Why isn’t a query using a parallel table scan?

[Permalink: Why isn’t a query using a parallel table scan?](#why-isnt-a-query-using-a-parallel-table-scan)

The planner doesn’t consider [out-of-line storage](https://www.postgresql.org/docs/current/storage-toast.html) in cost estimates, which can make a serial scan look cheaper. You can reduce the cost of a parallel scan for a query with:

```
BEGIN;
SET LOCAL min_parallel_table_scan_size = 1;
SET LOCAL parallel_setup_cost = 1;
SELECT ...
COMMIT;
```

or choose to store vectors inline:

```
ALTER TABLE items ALTER COLUMN embedding SET STORAGE PLAIN;
```

#### Why are there less results for a query after adding an HNSW index?

[Permalink: Why are there less results for a query after adding an HNSW index?](#why-are-there-less-results-for-a-query-after-adding-an-hnsw-index)

Results are limited by the size of the dynamic candidate list ( `hnsw.ef_search`), which is 40 by default. There may be even less results due to dead tuples or filtering conditions in the query. Enabling [iterative index scans](#iterative-index-scans) can help address this.

Also, note that `NULL` vectors are not indexed (as well as zero vectors for cosine distance).

#### Why are there less results for a query after adding an IVFFlat index?

[Permalink: Why are there less results for a query after adding an IVFFlat index?](#why-are-there-less-results-for-a-query-after-adding-an-ivfflat-index)

The index was likely created with too little data for the number of lists. Drop the index until the table has more data.

```
DROP INDEX index_name;
```

Results can also be limited by the number of probes ( `ivfflat.probes`). Enabling [iterative index scans](#iterative-index-scans) can address this.

Also, note that `NULL` vectors are not indexed (as well as zero vectors for cosine distance).

## Reference

[Permalink: Reference](#reference)

- [Vector](#vector-type)
- [Halfvec](#halfvec-type)
- [Bit](#bit-type)
- [Sparsevec](#sparsevec-type)

### Vector Type

[Permalink: Vector Type](#vector-type)

Each vector takes `4 * dimensions + 8` bytes of storage. Each element is a single-precision floating-point number (like the `real` type in Postgres), and all elements must be finite (no `NaN`, `Infinity` or `-Infinity`). Vectors can have up to 16,000 dimensions.

### Vector Operators

[Permalink: Vector Operators](#vector-operators)

| Operator | Description | Added |
| --- | --- | --- |
| + | element-wise addition |  |
| - | element-wise subtraction |  |
| \* | element-wise multiplication | 0.5.0 |
| \|\| | concatenate | 0.7.0 |
| <-> | Euclidean distance |  |
| <#> | negative inner product |  |
| <=> | cosine distance |  |
| <+> | taxicab distance | 0.7.0 |

### Vector Functions

[Permalink: Vector Functions](#vector-functions)

| Function | Description | Added |
| --- | --- | --- |
| binary\_quantize(vector) → bit | binary quantize | 0.7.0 |
| cosine\_distance(vector, vector) → double precision | cosine distance |  |
| inner\_product(vector, vector) → double precision | inner product |  |
| l1\_distance(vector, vector) → double precision | taxicab distance | 0.5.0 |
| l2\_distance(vector, vector) → double precision | Euclidean distance |  |
| l2\_normalize(vector) → vector | Normalize with Euclidean norm | 0.7.0 |
| subvector(vector, integer, integer) → vector | subvector | 0.7.0 |
| vector\_dims(vector) → integer | number of dimensions |  |
| vector\_norm(vector) → double precision | Euclidean norm |  |

### Vector Aggregate Functions

[Permalink: Vector Aggregate Functions](#vector-aggregate-functions)

| Function | Description | Added |
| --- | --- | --- |
| avg(vector) → vector | average |  |
| sum(vector) → vector | sum | 0.5.0 |

### Halfvec Type

[Permalink: Halfvec Type](#halfvec-type)

Each half vector takes `2 * dimensions + 8` bytes of storage. Each element is a half-precision floating-point number, and all elements must be finite (no `NaN`, `Infinity` or `-Infinity`). Half vectors can have up to 16,000 dimensions.

### Halfvec Operators

[Permalink: Halfvec Operators](#halfvec-operators)

| Operator | Description | Added |
| --- | --- | --- |
| + | element-wise addition | 0.7.0 |
| - | element-wise subtraction | 0.7.0 |
| \* | element-wise multiplication | 0.7.0 |
| \|\| | concatenate | 0.7.0 |
| <-> | Euclidean distance | 0.7.0 |
| <#> | negative inner product | 0.7.0 |
| <=> | cosine distance | 0.7.0 |
| <+> | taxicab distance | 0.7.0 |

### Halfvec Functions

[Permalink: Halfvec Functions](#halfvec-functions)

| Function | Description | Added |
| --- | --- | --- |
| binary\_quantize(halfvec) → bit | binary quantize | 0.7.0 |
| cosine\_distance(halfvec, halfvec) → double precision | cosine distance | 0.7.0 |
| inner\_product(halfvec, halfvec) → double precision | inner product | 0.7.0 |
| l1\_distance(halfvec, halfvec) → double precision | taxicab distance | 0.7.0 |
| l2\_distance(halfvec, halfvec) → double precision | Euclidean distance | 0.7.0 |
| l2\_norm(halfvec) → double precision | Euclidean norm | 0.7.0 |
| l2\_normalize(halfvec) → halfvec | Normalize with Euclidean norm | 0.7.0 |
| subvector(halfvec, integer, integer) → halfvec | subvector | 0.7.0 |
| vector\_dims(halfvec) → integer | number of dimensions | 0.7.0 |

### Halfvec Aggregate Functions

[Permalink: Halfvec Aggregate Functions](#halfvec-aggregate-functions)

| Function | Description | Added |
| --- | --- | --- |
| avg(halfvec) → halfvec | average | 0.7.0 |
| sum(halfvec) → halfvec | sum | 0.7.0 |

### Bit Type

[Permalink: Bit Type](#bit-type)

Each bit vector takes `dimensions / 8 + 8` bytes of storage. See the [Postgres docs](https://www.postgresql.org/docs/current/datatype-bit.html) for more info.

### Bit Operators

[Permalink: Bit Operators](#bit-operators)

| Operator | Description | Added |
| --- | --- | --- |
| <~> | Hamming distance | 0.7.0 |
| <%> | Jaccard distance | 0.7.0 |

### Bit Functions

[Permalink: Bit Functions](#bit-functions)

| Function | Description | Added |
| --- | --- | --- |
| hamming\_distance(bit, bit) → double precision | Hamming distance | 0.7.0 |
| jaccard\_distance(bit, bit) → double precision | Jaccard distance | 0.7.0 |

### Sparsevec Type

[Permalink: Sparsevec Type](#sparsevec-type)

Each sparse vector takes `8 * non-zero elements + 16` bytes of storage. Each element is a single-precision floating-point number, and all elements must be finite (no `NaN`, `Infinity` or `-Infinity`). Sparse vectors can have up to 16,000 non-zero elements.

### Sparsevec Operators

[Permalink: Sparsevec Operators](#sparsevec-operators)

| Operator | Description | Added |
| --- | --- | --- |
| <-> | Euclidean distance | 0.7.0 |
| <#> | negative inner product | 0.7.0 |
| <=> | cosine distance | 0.7.0 |
| <+> | taxicab distance | 0.7.0 |

### Sparsevec Functions

[Permalink: Sparsevec Functions](#sparsevec-functions)

| Function | Description | Added |
| --- | --- | --- |
| cosine\_distance(sparsevec, sparsevec) → double precision | cosine distance | 0.7.0 |
| inner\_product(sparsevec, sparsevec) → double precision | inner product | 0.7.0 |
| l1\_distance(sparsevec, sparsevec) → double precision | taxicab distance | 0.7.0 |
| l2\_distance(sparsevec, sparsevec) → double precision | Euclidean distance | 0.7.0 |
| l2\_norm(sparsevec) → double precision | Euclidean norm | 0.7.0 |
| l2\_normalize(sparsevec) → sparsevec | Normalize with Euclidean norm | 0.7.0 |

## Installation Notes - Linux and Mac

[Permalink: Installation Notes - Linux and Mac](#installation-notes---linux-and-mac)

### Postgres Location

[Permalink: Postgres Location](#postgres-location)

If your machine has multiple Postgres installations, specify the path to [pg\_config](https://www.postgresql.org/docs/current/app-pgconfig.html) with:

```
export PG_CONFIG=/Library/PostgreSQL/17/bin/pg_config
```

Then re-run the installation instructions (run `make clean` before `make` if needed). If `sudo` is needed for `make install`, use:

```
sudo --preserve-env=PG_CONFIG make install
```

A few common paths on Mac are:

- EDB installer - `/Library/PostgreSQL/17/bin/pg_config`
- Homebrew (arm64) - `/opt/homebrew/opt/postgresql@17/bin/pg_config`
- Homebrew (x86-64) - `/usr/local/opt/postgresql@17/bin/pg_config`

Note: Replace `17` with your Postgres server version

### Missing Header

[Permalink: Missing Header](#missing-header)

If compilation fails with `fatal error: postgres.h: No such file or directory`, make sure Postgres development files are installed on the server.

For Ubuntu and Debian, use:

```
sudo apt install postgresql-server-dev-17
```

Note: Replace `17` with your Postgres server version

### Missing SDK

[Permalink: Missing SDK](#missing-sdk)

If compilation fails and the output includes `warning: no such sysroot directory` on Mac, reinstall Xcode Command Line Tools.

### Portability

[Permalink: Portability](#portability)

By default, pgvector compiles with `-march=native` on some platforms for best performance. However, this can lead to `Illegal instruction` errors if trying to run the compiled extension on a different machine.

To compile for portability, use:

```
make OPTFLAGS=""
```

## Installation Notes - Windows

[Permalink: Installation Notes - Windows](#installation-notes---windows)

### Missing Header

[Permalink: Missing Header](#missing-header-1)

If compilation fails with `Cannot open include file: 'postgres.h': No such file or directory`, make sure `PGROOT` is correct.

### Permissions

[Permalink: Permissions](#permissions)

If installation fails with `Access is denied`, re-run the installation instructions as an administrator.

## Additional Installation Methods

[Permalink: Additional Installation Methods](#additional-installation-methods)

### Docker

[Permalink: Docker](#docker)

Get the [Docker image](https://hub.docker.com/r/pgvector/pgvector) with:

```
docker pull pgvector/pgvector:pg17
```

This adds pgvector to the [Postgres image](https://hub.docker.com/_/postgres) (replace `17` with your Postgres server version, and run it the same way).

You can also build the image manually:

```
git clone --branch v0.8.0 https://github.com/pgvector/pgvector.git
cd pgvector
docker build --pull --build-arg PG_MAJOR=17 -t myuser/pgvector .
```

### Homebrew

[Permalink: Homebrew](#homebrew)

With Homebrew Postgres, you can use:

```
brew install pgvector
```

Note: This only adds it to the `postgresql@17` and `postgresql@14` formulas

### PGXN

[Permalink: PGXN](#pgxn)

Install from the [PostgreSQL Extension Network](https://pgxn.org/dist/vector) with:

```
pgxn install vector
```

### APT

[Permalink: APT](#apt)

Debian and Ubuntu packages are available from the [PostgreSQL APT Repository](https://wiki.postgresql.org/wiki/Apt). Follow the [setup instructions](https://wiki.postgresql.org/wiki/Apt#Quickstart) and run:

```
sudo apt install postgresql-17-pgvector
```

Note: Replace `17` with your Postgres server version

### Yum

[Permalink: Yum](#yum)

RPM packages are available from the [PostgreSQL Yum Repository](https://yum.postgresql.org/). Follow the [setup instructions](https://www.postgresql.org/download/linux/redhat/) for your distribution and run:

```
sudo yum install pgvector_17
# or
sudo dnf install pgvector_17
```

Note: Replace `17` with your Postgres server version

### pkg

[Permalink: pkg](#pkg)

Install the FreeBSD package with:

```
pkg install postgresql16-pgvector
```

or the port with:

```
cd /usr/ports/databases/pgvector
make install
```

### conda-forge

[Permalink: conda-forge](#conda-forge)

With Conda Postgres, install from [conda-forge](https://anaconda.org/conda-forge/pgvector) with:

```
conda install -c conda-forge pgvector
```

This method is [community-maintained](https://github.com/conda-forge/pgvector-feedstock) by [@mmcauliffe](https://github.com/mmcauliffe)

### Postgres.app

[Permalink: Postgres.app](#postgresapp)

Download the [latest release](https://postgresapp.com/downloads.html) with Postgres 15+.

## Hosted Postgres

[Permalink: Hosted Postgres](#hosted-postgres)

pgvector is available on [these providers](https://github.com/pgvector/pgvector/issues/54).

## Upgrading

[Permalink: Upgrading](#upgrading)

[Install](#installation) the latest version (use the same method as the original installation). Then in each database you want to upgrade, run:

```
ALTER EXTENSION vector UPDATE;
```

You can check the version in the current database with:

```
SELECT extversion FROM pg_extension WHERE extname = 'vector';
```

## Upgrade Notes

[Permalink: Upgrade Notes](#upgrade-notes)

### 0.6.0

[Permalink: 0.6.0](#060)

#### Postgres 12

[Permalink: Postgres 12](#postgres-12)

If upgrading with Postgres 12, remove this line from `sql/vector--0.5.1--0.6.0.sql`:

```
ALTER TYPE vector SET (STORAGE = external);
```

Then run `make install` and `ALTER EXTENSION vector UPDATE;`.

#### Docker

[Permalink: Docker](#docker-1)

The Docker image is now published in the `pgvector` org, and there are tags for each supported version of Postgres (rather than a `latest` tag).

```
docker pull pgvector/pgvector:pg16
# or
docker pull pgvector/pgvector:0.6.0-pg16
```

Also, if you’ve increased `maintenance_work_mem`, make sure `--shm-size` is at least that size to avoid an error with parallel HNSW index builds.

```
docker run --shm-size=1g ...
```

## Thanks

[Permalink: Thanks](#thanks)

Thanks to:

- [PASE: PostgreSQL Ultra-High-Dimensional Approximate Nearest Neighbor Search Extension](https://dl.acm.org/doi/pdf/10.1145/3318464.3386131)
- [Faiss: A Library for Efficient Similarity Search and Clustering of Dense Vectors](https://github.com/facebookresearch/faiss)
- [Using the Triangle Inequality to Accelerate k-means](https://cdn.aaai.org/ICML/2003/ICML03-022.pdf)
- [k-means++: The Advantage of Careful Seeding](https://theory.stanford.edu/~sergei/papers/kMeansPP-soda.pdf)
- [Concept Decompositions for Large Sparse Text Data using Clustering](https://www.cs.utexas.edu/users/inderjit/public_papers/concept_mlj.pdf)
- [Efficient and Robust Approximate Nearest Neighbor Search using Hierarchical Navigable Small World Graphs](https://arxiv.org/ftp/arxiv/papers/1603/1603.09320.pdf)

## History

[Permalink: History](#history)

View the [changelog](https://github.com/pgvector/pgvector/blob/master/CHANGELOG.md)

## Contributing

[Permalink: Contributing](#contributing)

Everyone is encouraged to help improve this project. Here are a few ways you can help:

- [Report bugs](https://github.com/pgvector/pgvector/issues)
- Fix bugs and [submit pull requests](https://github.com/pgvector/pgvector/pulls)
- Write, clarify, or fix documentation
- Suggest or add new features

To get started with development:

```
git clone https://github.com/pgvector/pgvector.git
cd pgvector
make
make install
```

To run all tests:

```
make installcheck        # regression tests
make prove_installcheck  # TAP tests
```

To run single tests:

```
make installcheck REGRESS=functions                            # regression test
make prove_installcheck PROVE_TESTS=test/t/001_ivfflat_wal.pl  # TAP test
```

To enable assertions:

```
make clean && PG_CFLAGS="-DUSE_ASSERT_CHECKING" make && make install
```

To enable benchmarking:

```
make clean && PG_CFLAGS="-DIVFFLAT_BENCH" make && make install
```

To show memory usage:

```
make clean && PG_CFLAGS="-DHNSW_MEMORY -DIVFFLAT_MEMORY" make && make install
```

To get k-means metrics:

```
make clean && PG_CFLAGS="-DIVFFLAT_KMEANS_DEBUG" make && make install
```

Resources for contributors

- [Extension Building Infrastructure](https://www.postgresql.org/docs/current/extend-pgxs.html)
- [Index Access Method Interface Definition](https://www.postgresql.org/docs/current/indexam.html)
- [Generic WAL Records](https://www.postgresql.org/docs/current/generic-wal.html)

## About

Open-source vector similarity search for Postgres


### Topics

[nearest-neighbor-search](/topics/nearest-neighbor-search "Topic: nearest-neighbor-search") [approximate-nearest-neighbor-search](/topics/approximate-nearest-neighbor-search "Topic: approximate-nearest-neighbor-search")

### Resources

[Readme](#readme-ov-file)

### License

[View license](#License-1-ov-file)

### Security policy

[Security policy](#security-ov-file)

[Activity](/pgvector/pgvector/activity)

[Custom properties](/pgvector/pgvector/custom-properties)

### Stars

[**12.9k**\\
stars](/pgvector/pgvector/stargazers)

### Watchers

[**104**\\
watching](/pgvector/pgvector/watchers)

### Forks

[**608**\\
forks](/pgvector/pgvector/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fpgvector%2Fpgvector&report=pgvector+%28user%29)

## [Releases](/pgvector/pgvector/releases)

[36tags](/pgvector/pgvector/tags)

## [Packages\  0](/orgs/pgvector/packages?repo_name=pgvector)

No packages published

## [Contributors\  19](/pgvector/pgvector/graphs/contributors)

- [![@ankane](https://avatars.githubusercontent.com/u/220358?s=64&v=4)](https://github.com/ankane)
- [![@hlinnaka](https://avatars.githubusercontent.com/u/191602?s=64&v=4)](https://github.com/hlinnaka)
- [![@jkatz](https://avatars.githubusercontent.com/u/1694?s=64&v=4)](https://github.com/jkatz)
- [![@Ngalstyan4](https://avatars.githubusercontent.com/u/4647374?s=64&v=4)](https://github.com/Ngalstyan4)
- [![@fanfuxiaoran](https://avatars.githubusercontent.com/u/4902937?s=64&v=4)](https://github.com/fanfuxiaoran)
- [![@nathan-bossart](https://avatars.githubusercontent.com/u/25780657?s=64&v=4)](https://github.com/nathan-bossart)
- [![@nodomain](https://avatars.githubusercontent.com/u/104389?s=64&v=4)](https://github.com/nodomain)
- [![@mulander](https://avatars.githubusercontent.com/u/107247?s=64&v=4)](https://github.com/mulander)
- [![@jeff-davis](https://avatars.githubusercontent.com/u/214386?s=64&v=4)](https://github.com/jeff-davis)
- [![@SamuelMarks](https://avatars.githubusercontent.com/u/807580?s=64&v=4)](https://github.com/SamuelMarks)
- [![@tucnak](https://avatars.githubusercontent.com/u/934682?s=64&v=4)](https://github.com/tucnak)
- [![@wlaurance](https://avatars.githubusercontent.com/u/1059214?s=64&v=4)](https://github.com/wlaurance)
- [![@Florents-Tselai](https://avatars.githubusercontent.com/u/2118708?s=64&v=4)](https://github.com/Florents-Tselai)
- [![@yihong0618](https://avatars.githubusercontent.com/u/15976103?s=64&v=4)](https://github.com/yihong0618)

[\+ 5 contributors](/pgvector/pgvector/graphs/contributors)

## Languages

- [C77.0%](/pgvector/pgvector/search?l=c)
- [Perl22.3%](/pgvector/pgvector/search?l=perl)
- Other0.7%

You can’t perform that action at this time.