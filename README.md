```bash
duckdb -c \  
  "select license->>'key' as license, count(*) as count \
  from read_json('https://api.github.com/orgs/slcpython/repos') \
  group by 1 \
  order by count desc"
```