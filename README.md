# Satellite Tracker Toolkit

A Python toolkit for importing, validating, searching, analysing, and visualising satellite tracker data.

The toolkit is designed to work alongside my [Java Satellite Tracker](https://github.com/Aidan-Cossu/satellite-tracker-v1) and provides a separate environment for analysing the data produced by the application

## Features

- Import satellite tracking data from SQL database
- Import satellite tracking data from CSV
- Validate satellite data and detect invalid values
- Search and filter satellite observations
- Analyse altitude, velocity, and observation frequency
- Calculate observation durations and distances
- Detect irregular observations
- Generate statistical summaries
- Visualise satellite data with charts
- Export processed results

The toolkit is intentionally separate from the Java application. The Java application focuses on tracking and visualisation, while the Python toolkit focuses on data analysis and validation.

**Both projects can also be used independently. The toolkit can analyse compatible satellite data without the Java application, and the Java application does not require the Python toolkit to run.**

## Technologies

- Python
- Matplotlib
- CSV
- SQL data exported from the Java application

## Future Development
The toolkit will eventually be used to also validate and analyse the output of my future C++ Orbit Propagation Engine.

## Related Projects

- [Satellite Tracker](https://github.com/Aidan-Cossu/satellite-tracker-v1) - Java application for real-time satellite tracking and visualisation
