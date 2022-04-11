Switch to at least java 8. This example uses Java 17:
```
jenv local openjdk64-17
```

The model was from https://groups.google.com/g/jaamsim-users/c/wg7MizfuxYw/m/iJ599D4-AQAJ.

Run the simulation in headless mode:
```
cat A_1-rwy_v10.cfg | java -jar JaamSim2022-02.jar -s -h
```
