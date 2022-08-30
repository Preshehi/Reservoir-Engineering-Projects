# Reservoir Engineering Projects

# Cassandra
This is an app I developed to estimate the critical drawdown at the onset of sand production in an unconsolidated reservoir. It follows a mathematical model which was also developed by me and published in the SPE paper titled "Cassandra: A Model and Simulator Developed for Critical Drawdown Estimation in Unconsolidated Reservoirs".

It requests for a few inputs including reservoir pressure as well as stress parameters of the formation which can be inferred from log data or can be estimated from core analysis. The primary result is the critical drawdown which is the pressure differential that would cause sand production to occur, however, it has also been extended to estimate flow rate. In order to estimate flow rate, some more parameters will be required including fluid type, viscosity, permeability and so on.

The main file is the Cassandra.py while others are supporting modules which help in error handling as well as providing guidance in the use of the software and providing more details about the software.
