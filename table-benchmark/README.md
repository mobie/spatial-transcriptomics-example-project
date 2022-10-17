# Table Loading Benchmarks

## Loading a single big transcriptomics table

**Loading from filesystem**: (statistics across 10 runs)
```
Min: 0.056575775146484375 s
Max: 0.0599818229675293 s
Mean: 0.057353544235229495 +- 0.0009124553183889059 s
```

**Loading from github**: (statistics across 10 runs)


Comparison:
- loading view with the table in MoBIE locally:
- loading view with the table in MoBIE from github:


## Loading many big transcriptomics tables (40)

**Loading from filesystem**: (statistics across 5 runs)
Min: 5.252879858016968 s
Max: 5.372411251068115 s
Mean: 5.284460020065308 +- 0.04501603022028916 s

Comparison:
- loading view with all the tables in MoBIE locally takes: 451280 ms: 451 sec: ~ 7.5 min
