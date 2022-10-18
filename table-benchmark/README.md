# Table Loading Benchmarks

## TSV

### Loading a single big transcriptomics table

**loading from filesystem**: (statistics across 10 runs)
```
min: 0.056575775146484375 s
max: 0.0599818229675293 s
mean: 0.057353544235229495 +- 0.0009124553183889059 s
```

**Loading from github**: (statistics across 10 runs)
```
Min: 0.311129093170166 s
Max: 0.6253552436828613 s
Mean: 0.35982043743133546 +- 0.08919928117656666 s
```


Comparison:
- loading view with the table in MoBIE locally: 7567 ms: 7.5 sec
- loading view with the table in MoBIE from github: 7866 ms: 7.8 sec


### Loading many big transcriptomics tables (40)

**Loading from filesystem**: (statistics across 5 runs)
```
Min: 5.252879858016968 s
Max: 5.372411251068115 s
Mean: 5.284460020065308 +- 0.04501603022028916 s
```

Comparison:
- loading view with all the tables in MoBIE locally takes: 451280 ms: 451 sec: ~ 7.5 min


## Parquet

**loading from filesystem**: (statistics across 10 runs)
```
Min: 0.017370939254760742 s
Max: 0.0660090446472168 s
Mean: 0.022612929344177246 +- 0.014466204763517261
```
