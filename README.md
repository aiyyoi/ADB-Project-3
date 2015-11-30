# ADB-Project-2
###COMS 6111 Advanced Database Systems Project 3: 
######Association Rule Mining


By:

Xuejun Wang, UNI: xw2355

Akshaan Kakar, UNI: ak3808

## Essential Information

### List of Files in Submission
<pre><code>

</code></pre>

### Compile/ Run Instructions
1. From terminal, change file path to the project root folder
2. To run:<pre><code>python MainScript.py -data ./integrated-dataset.csv  -msuo 0.25 -mconf 0.8</code></pre>
4. The output will be written to a file named output.txt

## Dataset Generation 
The dataset we decided to use for this project was created by joining to datasets from the NYC open dataset repositories. These were as follows:
1. [Parking violation codes] (https://data.cityofnewyork.us/Transportation/DOF-Parking-Violation-Codes/ncbg-6agr)
2. [Parking violations in the fiscal year 2013-2014] (https://data.cityofnewyork.us/City-Government/Parking-Violations-Issued-Fiscal-Year-2014-August-/jt7v-77mi)

We joined the two files on the violation code field so that we could have the description of each parking violation as well as the dollar value of the fine for each violation against each violation incident decribed in the second dataset.

We then dropped columns that were uninteresting or redundant and retained only the following columns:  
1. RegistrationState - State in which vehicle is registered  
2. [PlateType - Type of license plate] (http://www.nyc.gov/html/dof/html/pdf/faq/stars_codes.pdf)  
3. ViolationCode - Parking violation code  
4. VehicleBodyType - Type of vehicle (Sedan, SUV etc.)
5. VehicleMake - Name of Vehicle manufacturer  
6. ViolationPrecinct - The NYC precinct in which the violation occurred  
7. ViolationCounty - The county in which the violation ocurred
8. VehicleColor - Color of the vehicle
9. ManhattanBelow96 - The fine for this offence below 96th street
10. OtherAreas - The fine for this offence in other areas
11. DEFINITION - The description in words of the parking violation

Finally, we appended the name of each column to the actual values in each column so that the rules we output were easy to understand. If this measure was not taken, then the numerical values output in the final association rules would be ambiguous.

From this dataset, we expected to derive high confidence assocation rules that could tell us things like:
1. A certain car type is more likely to commit a certain parking violation
2. A certain parking violation is seen more often in a particluar county/precinct
3. The most common fine value for a certain kind of car is X dollars



## Internal Design
**MainScript.py** : The main script starts by parsing input arguments: URL of the dataset, support and confidence threshold value for Apriori algorithm implementation, and delegates to **LargeItemsetGenerator** class. It then takes the returned large itemsets and extracts the final, high-confidence association rules from them. This is done as described in the reference paper on the Apriori Algorithm. Every subset a of every large itemset l is considered and those subsets with support(l)/support(a) > minconf are output as high confidence rules a => (l-a). Since we only wanted rules with one item on the right, we did not consider subsets for which (l-a) is larger than on element.

**MemberClass** : This wrapper class is used to hold the large item sets and their corresponding support count values. The objects of this class have two attributes  
1. A list that holds the items belonging to the itemset.
2. An integer denoting the absolute support count of this itemset.

**LargeItemsetGenerator** :  #TODO

**CandidateItemsetGenerator** : #TODO

**Apriori.py** : #TODO

## Interesting Parameters and REsults
An interesting set of parameters used is as follows:
Minimum support : 0.05
Minimum confidence : 0.8

This set of parameters results in a large number of high-confidence rules. Some interesting rules obtained are a follows:

[$65, RegState-NY, $35, PlateType-PAS] => [Muni Meter --
(37) Parking in excess of the allowed time
(38) Failing to show a receipt or tag in the windshield
Drivers get a 5-minute grace period past the expired time on Muni-Meter receipts.] (Conf: 99.9924374196%, Supp: 20.1810217196%)

This rules tells us that if a car is Registered in NY and has a PAS plate and has paid a fine of either $65 below 96th street or $35 in other areas, then the violation committed is most likely (37) or (38).

Another example of an interesting rule we obtained is as follows:

[VehicleBodyType-SUBN] => [PlateType-PAS] (Conf: 83.7701379789%, Supp: 33.1745959064%)

If a vehicle has a suburban body type, it is highly likely to have a PAS plate type. This is interesting because we can predict the plate type of a vehicle from the body type (in this case, a suburban body type is highly likely to have a PAS plate type).

## References
1. Rakesh Agrawal and Ramakrishnan Srikant: Fast Algorithms for Mining Association Rules in Large Databases, VLDB 1994.
