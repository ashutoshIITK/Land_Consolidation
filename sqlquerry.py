query = """--
-- Table structure for table `C.H. Form 1-A`
--
CREATE TABLE `C.H. Form 1-A` (
  `Serial No` int(11) DEFAULT NULL,
  `Villages` varchar(255) DEFAULT NULL,
  `Name of the villages` varchar(255) DEFAULT NULL,
  `Name od District` varchar(255) DEFAULT NULL,
  `Name of Tehsil` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 2-a`
--
CREATE TABLE `C.H. Form 2-A-1` (
  `Plot No` varchar(255) DEFAULT NULL,
  `As found on spot` varchar(255) DEFAULT NULL,
  `Details of uncultivated area (Nature)` varchar(255) DEFAULT NULL,
  `Details of uncultivated area (Included in holding)` varchar(255) DEFAULT NULL,
  `Details of uncultivated area (not included in holding)` varchar(255) DEFAULT NULL,
  `Source` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Method` varchar(255) DEFAULT NULL,
  `Irrigable area` varchar(255) DEFAULT NULL,
  `Kharif` varchar(255) DEFAULT NULL,
  `Rabi` varchar(255) DEFAULT NULL,
  `Zaid` varchar(255) DEFAULT NULL,
  `Physical features of the plot` varchar(255) DEFAULT NULL,
  `Solid class in current settlement` varchar(255) DEFAULT NULL,
  `Area (Non consolidable)` varchar(255) DEFAULT NULL,
  `Area (Consolidable)` varchar(255) DEFAULT NULL,
  `Exchange ratio in annas (in words)` varchar(255) DEFAULT NULL,
  `Valutaion of the consolidable area of the plot (col27 x col28)` varchar(255) DEFAULT NULL,
  `Modified exchange ratio` varchar(255) DEFAULT NULL,
  `Valuation as modified by superior authorities (col27 X col30)` varchar(255) DEFAULT NULL,
  `Khata no (As proposed by ACO )` varchar(255) DEFAULT NULL,
  `Khata no (As modified by CO)` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 2-a`
--
CREATE TABLE `C.H. Form 2-A-2` (
  `Id` varchar(255) DEFAULT NULL,
  `Plot No` varchar(255) DEFAULT NULL,
  `Description` varchar(255) DEFAULT NULL,
  `Measurement` varchar(255) DEFAULT NULL,
  `Age` varchar(255) DEFAULT NULL,
  `Estimated Value` varchar(255) DEFAULT NULL,
  `Name of owner` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Share` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 2-a`
--
CREATE TABLE `C.H. Form 2-A-3` (
  `Id` varchar(255) DEFAULT NULL,
  `Plot No` varchar(255) DEFAULT NULL,
  `Nature` varchar(255) DEFAULT NULL,
  `Area` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 4`
--
CREATE TABLE `C.H. Form 4` (
  `ID` int(11) DEFAULT NULL,
  `No of Khata Khatauni of the basic year` int(11) DEFAULT NULL,
  `Plot Nos where mistakes and disputes donot relate to the whole K` int(11) DEFAULT NULL,
  `Areas of plots recorded in column 2` int(11) DEFAULT NULL,
  `Serial No (Deatails of mistakes and disputes)` int(11) DEFAULT NULL,
  `Details` mediumtext,
  `Details of shares claimed in the holding by each tenure-holder` varchar(255) DEFAULT NULL,
  `Orders od Assistant Consolidation Office` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 5 (extract)`
--
CREATE TABLE `C.H. Form 5(Extract)` (
  `No of Khata in the current Annual Register` varchar(255) DEFAULT NULL,
  `Name of tenure-holder` varchar(255) DEFAULT NULL,
  `Claass of tenure` varchar(255) DEFAULT NULL,
  `Year of commencement of tenre` varchar(255) DEFAULT NULL,
  `Plot no` varchar(255) DEFAULT NULL,
  `Total` varchar(255) DEFAULT NULL,
  `Area (Consolidable)` varchar(255) DEFAULT NULL,
  `Area (Non-Consolidable)` varchar(255) DEFAULT NULL,
  `Exchange ratio in annas (in words) of consolidable areas (Col 8)` varchar(255) DEFAULT NULL,
  `Valuation in annasof the consolidable area` varchar(255) DEFAULT NULL,
  `Description (Details of improvement)` varchar(255) DEFAULT NULL,
  `Measurement (Details of improvement)` varchar(255) DEFAULT NULL,
  `Estimated value (Details of improvement)` varchar(255) DEFAULT NULL,
  `Name of the owner,address and share in the property` varchar(255) DEFAULT NULL,
  `Land revenue payable by the tenure holder` varchar(255) DEFAULT NULL,
  `Name with percentage and residance (Details of Asami)` varchar(255) DEFAULT NULL,
  `Year of commencement of tenure (Details of Asami)` varchar(255) DEFAULT NULL,
  `Rent payable` varchar(255) DEFAULT NULL,
  `Details of mistakes and disputes discovered and share recorded` varchar(255) DEFAULT NULL,
  `Remarks` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 5-b`
--
CREATE TABLE `C.H. Form 5-B` (
  `ID` int(11) DEFAULT NULL,
  `Plot No` int(11) DEFAULT NULL,
  `No of Khata of current Annual Register` int(11) DEFAULT NULL,
  `Name of the person recorded in annual register` varchar(255) DEFAULT NULL,
  `Name of the person alleged to be in possession` varchar(255) DEFAULT NULL,
  `Total` int(11) DEFAULT NULL,
  `Non-consolidable` int(11) DEFAULT NULL,
  `Consolidable` int(11) DEFAULT NULL,
  `Exchange ratio in annas (in words)in consolidable area` int(11) DEFAULT NULL,
  `Annual valuation` int(11) DEFAULT NULL,
  `Class` int(11) DEFAULT NULL,
  `Measurements and age` int(11) DEFAULT NULL,
  `Estimated value` double DEFAULT NULL,
  `Name and the owner, his address and share in property` varchar(255) DEFAULT NULL,
  `Details of mistakes of area,if any` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 6`
--
CREATE TABLE `C.H. Form 6` (
  `ID` int(11) DEFAULT NULL,
  `Case no` int(11) DEFAULT NULL,
  `Village and pragana` varchar(255) DEFAULT NULL,
  `Name of parties` varchar(255) DEFAULT NULL,
  `Description of the case` varchar(255) DEFAULT NULL,
  `Date of instituition` datetime DEFAULT NULL,
  `Date of order` datetime DEFAULT NULL,
  `Gist of orders passes regarding (Partition and amalgamation)` varchar(255) DEFAULT NULL,
  `Gist of orders passes regarding (Other matters)` varchar(255) DEFAULT NULL,
  `Dates of Amaldaramad of orders mentioned in (Column 7)` datetime DEFAULT NULL,
  `Dates of Amaldaramad of orders mentioned in (Column 8)` datetime DEFAULT NULL,
  `No and date of chalan` varchar(255) DEFAULT NULL,
  `Official's signature and date of dilivery` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 10-a`
--
CREATE TABLE `C.H. Form 10-A` (
  `Serial No` int(11) DEFAULT NULL,
  `Name of tenure-holder with percentage and residance` varchar(255) DEFAULT NULL,
  `No of Khata Khatauni` int(11) DEFAULT NULL,
  `Class of tenure` varchar(255) DEFAULT NULL,
  `Land revenue` double DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 11`
--
CREATE TABLE `C.H. Form 11` (
  `Serial No` int(11) DEFAULT NULL,
  `Serial Number in basic Khatauni` int(11) DEFAULT NULL,
  `Name of the tenure hollder` varchar(255) DEFAULT NULL,
  `Share of tenure holder` int(11) DEFAULT NULL,
  `Land revenue payable by the tenure-holder shown in column 8` double DEFAULT NULL,
  `Number of tenure-holder` int(11) DEFAULT NULL,
  `Number of each plot/area` int(11) DEFAULT NULL,
  `Land revenue payable by the tenure-holder shown in column 10` double DEFAULT NULL,
  `Date of order and case number >>` varchar(255) DEFAULT NULL,
  `Plot Number` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Land revenue payable` double DEFAULT NULL,
  `Serial nnumber (Col 1)cof Khatas amalgamated` int(11) DEFAULT NULL,
  `Name of tenure-holders anddetails of shares in amalgamated Khata` varchar(255) DEFAULT NULL,
  `Date of order and case number` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 18`
--
CREATE TABLE `C.H. Form 18` (
  `Seral No` int(11) DEFAULT NULL,
  `Number od plot` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Number of Khata Khatauni` int(11) DEFAULT NULL,
  `Remarks showing cause of exclusion` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 23 (part i)`
--
CREATE TABLE `C.H. Form 23(Part I)` (
  `Serial No` int(11) DEFAULT NULL,
  `Name and percentage of tenure-holder with residance` varchar(255) DEFAULT NULL,
  `Class of tenure` varchar(255) DEFAULT NULL,
  `Year of commencement of tenure` int(11) DEFAULT NULL,
  `Khata number of the revised Annulal Register in CH Form 11` int(11) DEFAULT NULL,
  `Plot No` int(11) DEFAULT NULL,
  `Total` int(11) DEFAULT NULL,
  `Area (Excluded from consolidation)` int(11) DEFAULT NULL,
  `Area (Included in consolidation)` int(11) DEFAULT NULL,
  `Exchange ratio of the plot or its part to be consolidated` int(11) DEFAULT NULL,
  `Anna valuatioin of the plot or its part to be consolidated` double DEFAULT NULL,
  `Land Revenue of the holding` double DEFAULT NULL,
  `Contribution inn terms of Anna valuation for public purposes` double DEFAULT NULL,
  `Contribution for public purposes in terms of area (Col 13X9/11)` double DEFAULT NULL,
  `Land revenue to be reduced` double DEFAULT NULL,
  `Amount of compensation` double DEFAULT NULL,
  `Net valuation to be alloted (Col 11X13)(on totals of holding)` double DEFAULT NULL,
  `Class of tenure (Proposed Holding)` varchar(255) DEFAULT NULL,
  `Plot no (Proposed Holding)` int(11) DEFAULT NULL,
  `Area (Proposed Holding)` int(11) DEFAULT NULL,
  `Exchange ratio (Proposed Holding)` int(11) DEFAULT NULL,
  `Annual valuation (Proposed Holding)` double DEFAULT NULL,
  `Land revenue payable by tenure-holder after reduction` double DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 23 (part iii)`
--
CREATE TABLE `C.H. Form 23(Part III)` (
  `Si No` int(11) DEFAULT NULL,
  `Purposes (From holding area)` varchar(255) DEFAULT NULL,
  `Plot No (From holding area)` int(11) DEFAULT NULL,
  `Area (From holding area)` int(11) DEFAULT NULL,
  `Purposes (From non-holding area)` varchar(255) DEFAULT NULL,
  `Plot No (From non-holding area)` int(11) DEFAULT NULL,
  `Area (From non-holding area)` int(11) DEFAULT NULL,
  `Plot No` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Particulars` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 23-a (part i)`
--
CREATE TABLE `C.H. Form 23-A(Part I)` (
  `Serial No` int(11) DEFAULT NULL,
  `Name and percentage of tenure-holder with residance` varchar(255) DEFAULT NULL,
  `Class of tenure` varchar(255) DEFAULT NULL,
  `No of Khata Khatauni` int(11) DEFAULT NULL,
  `Plot Number` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Land revenue` double DEFAULT NULL,
  `Name of encumbrancer and nature  of encumbrance` varchar(255) DEFAULT NULL,
  `Amount` double DEFAULT NULL,
  `Name and percentage with residance` varchar(255) DEFAULT NULL,
  `Plot No (Asami)` int(11) DEFAULT NULL,
  `Area (Asami)` int(11) DEFAULT NULL,
  `Rent payable (Asami)` double DEFAULT NULL,
  `Class of tenure (Proposed Holding)` varchar(255) DEFAULT NULL,
  `Plot No (Proposed Holding)` int(11) DEFAULT NULL,
  `Area alloted (Proposed Holding)` int(11) DEFAULT NULL,
  `Land Revenue (Proposed Holding)` double DEFAULT NULL,
  `Name of encumbrancer and nature of encumbrances` varchar(255) DEFAULT NULL,
  `Amount (Proposed Holding)` double DEFAULT NULL,
  `Name and percentage with residance >>` varchar(255) DEFAULT NULL,
  `Plot No(Assami ,if any,under tenure holder)` varchar(255) DEFAULT NULL,
  `Area (Assami ,if any,under tenure holder)` int(11) DEFAULT NULL,
  `Rent payable (Assami ,if any,under tenure holder)` double DEFAULT NULL,
  `No and kinds of trees,wellor other improvements` varchar(255) DEFAULT NULL,
  `Plot No on which trees etc exist` int(11) DEFAULT NULL,
  `Compensation` double DEFAULT NULL,
  `To whom payable` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 23-a (part ii)`
--
CREATE TABLE `C.H. Form 23-A(Part II)` (
  `Serial No` int(11) DEFAULT NULL,
  `Purposes (From Holding Area)` varchar(255) DEFAULT NULL,
  `Plot No (From Holding Area)` int(11) DEFAULT NULL,
  `Area (From Holding Area)` int(11) DEFAULT NULL,
  `Purposes (From non-holding Area)` varchar(255) DEFAULT NULL,
  `Plot No  (From non-holding Area)` int(11) DEFAULT NULL,
  `Area  (From non-holding Area)` int(11) DEFAULT NULL,
  `Plot No (Details ohther than land belonging to Gaon Sabha)` int(11) DEFAULT NULL,
  `Area  (Details ohther than land belonging to Gaon Sabha)` int(11) DEFAULT NULL,
  `Particulars  (Details ohther than land belonging to Gaon Sabha)` varchar(255) DEFAULT NULL,
  `Remarks  (Details ohther than land belonging to Gaon Sabha)` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 26`
--
CREATE TABLE `C.H. Form 26` (
  `ID` int(11) DEFAULT NULL,
  `Plot No on which the trees etc exist` int(11) DEFAULT NULL,
  `No and kind of trees,wells or other improvements` int(11) DEFAULT NULL,
  `Amount of compensation payable` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 26-a`
--
CREATE TABLE `C.H. Form 26-A` (
  `Serial No of the list` int(11) DEFAULT NULL,
  `Serial No of entry in CH form 23` int(11) DEFAULT NULL,
  `Name of the tenure-holder` varchar(255) DEFAULT NULL,
  `Amount of compensation` double DEFAULT NULL,
  `Amount adjusted towards cost of consolidation` double DEFAULT NULL,
  `Amount payable in cash` double DEFAULT NULL,
  `Date of payement` datetime DEFAULT NULL,
  `Amount paid` double DEFAULT NULL,
  `Signature of recipient` varchar(255) DEFAULT NULL,
  `Signature of Assistant Consolidation Officer who paid the amount` varchar(255) DEFAULT NULL,
  `Remarks` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 35`
--
CREATE TABLE `C.H. Form 35` (
  `ID` int(11) DEFAULT NULL,
  `Serial Number` varchar(255) DEFAULT NULL,
  `Name of paying compensation tenure-holder colum 16 of CH Form 32` int(11) DEFAULT NULL,
  `Plot Number` int(11) DEFAULT NULL,
  `Amount of Compensation Payable` int(11) DEFAULT NULL,
  `Serial Number-2` int(11) DEFAULT NULL,
  `Name of paying compensation tenure-holder Column 18 of CH Form32` int(11) DEFAULT NULL,
  `Plot Number-2` int(11) DEFAULT NULL,
  `Amount of compensation payable-2` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 41`
--
CREATE TABLE `C.H. Form 41` (
  `ID` int(11) DEFAULT NULL,
  `New Number` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Old Number` int(11) DEFAULT NULL,
  `Area-2` int(11) DEFAULT NULL,
  `New Khata-Khatauni Number` int(11) DEFAULT NULL,
  `Soil Class of last settlement` varchar(255) DEFAULT NULL,
  `Source of irrigation` varchar(255) DEFAULT NULL,
  `Remarks` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 45`
--
CREATE TABLE `C.H. Form 45` (
  `ID` int(11) DEFAULT NULL,
  `Serial Number of Khatauni Khata` int(11) DEFAULT NULL,
  `Name of tenure-holder with parentage and residence` varchar(255) DEFAULT NULL,
  `Year of commencement of tenure` int(11) DEFAULT NULL,
  `New plot Numbers` int(11) DEFAULT NULL,
  `Area` int(11) DEFAULT NULL,
  `Land Revenue of rent payable by the tenure-holder` int(11) DEFAULT NULL,
  `Remarks` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `Khasra`
--
CREATE TABLE `Khasra` (
  `Plot no.` varchar(255) DEFAULT NULL,
  `Khatauni no.` varchar(255) DEFAULT NULL,
  `Source of Irrigation` varchar(255) DEFAULT NULL,
  `Kharif crop Name` varchar(255) DEFAULT NULL,
  `Kharif crop irrigated area` varchar(255) DEFAULT NULL,
  `Kharif crop non-irrigated ares` varchar(255) DEFAULT NULL,
  `Rabi crop Name` varchar(255) DEFAULT NULL,
  `Rabi crop irrigated area` varchar(255) DEFAULT NULL,
  `Rabi crop non-irrigated ares` varchar(255) DEFAULT NULL,
  `Zaid crop Name` varchar(255) DEFAULT NULL,
  `Zaid crop irrigated area` varchar(255) DEFAULT NULL,
  `Zaid crop non-irrigated ares` varchar(255) DEFAULT NULL,
  `Two crop irrigated area` varchar(255) DEFAULT NULL,
  `Two crop non-irrigated area` varchar(255) DEFAULT NULL,
  `Description of trees` varchar(255) DEFAULT NULL,
  `Remark` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `Khatauni 1`
--
CREATE TABLE `Khatauni 1` (
  `Khatauni no.` varchar(255) DEFAULT NULL,
  `Total area` varchar(255) DEFAULT NULL,
  `Lagan` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `Khatauni 2`
--
CREATE TABLE `Khatauni 2` (
  `Id` varchar(255) DEFAULT NULL,
  `Khatauni no.` varchar(255) DEFAULT NULL,
  `Name of holder` varchar(255) DEFAULT NULL,
  `Name of father/husband/guardian` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `Khatauni 3`
--
CREATE TABLE `Khatauni 3` (
  `Id` varchar(255) DEFAULT NULL, 
  `Khatauni no.` varchar(255) DEFAULT NULL,
  `Fasli Year` varchar(255) DEFAULT NULL,
  `Khasra/Plot No.` varchar(255) DEFAULT NULL,
  `Plot Area` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 4a`
--
CREATE TABLE `CHForm4A1` (
  `Khatauni no.` varchar(255) DEFAULT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Father Name` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Share Claimed` varchar(255) DEFAULT NULL,
  `Error no.` varchar(255) DEFAULT NULL,
  `Error Detail` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 4a`
--
CREATE TABLE `CHForm4A2` (
  `Khatauni No.` varchar(255) DEFAULT NULL,   
  `Share Error no.` varchar(255) DEFAULT NULL,
  `Other Error No.` varchar(255) DEFAULT NULL,
  `Other Error Detail` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 4b`
--
CREATE TABLE `CHForm4B1` (
  `Khatauni no.` varchar(255) DEFAULT NULL,
  `Plot No.` varchar(255) DEFAULT NULL,
  `Area in Khatauni` varchar(255) DEFAULT NULL,
  `Area on Spot` varchar(255) DEFAULT NULL,
  `Error no.` varchar(255) DEFAULT NULL,  
  `Error Detail` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `ch form 4b`
--
CREATE TABLE `CHForm4B2` (
  `Khatauni No.` varchar(255) DEFAULT NULL,
  `Other Error No.` varchar(255) DEFAULT NULL,
  `Other Error Detail` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `CHForm11 1`
--
CREATE TABLE `CHForm11 1` (
  `Serial no.` varchar(255) DEFAULT NULL,
  `Fasli Year` varchar(255) DEFAULT NULL, 
  `Plot No.` varchar(255) DEFAULT NULL,
  `Area` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `CHForm11 2`
--
CREATE TABLE `CHForm11 2` (
  `Serial no.` varchar(255) DEFAULT NULL,
  `Name` varchar(255) DEFAULT NULL, 
  `Father Name` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Holder Name` varchar(255) DEFAULT NULL,
  `Share` varchar(255) DEFAULT NULL,
  `Devided Lagan` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `CHForm11 3`
--
CREATE TABLE `CHForm11 3` (
  `Serial no.` varchar(255) DEFAULT NULL,
  `Name(private property)` varchar(255) DEFAULT NULL, 
  `Plot No./Area` varchar(255) DEFAULT NULL,
  `Lagan` varchar(255) DEFAULT NULL,
  `Order By` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `CHForm11 4`
--
CREATE TABLE `CHForm11 4` (
  `Serial no.` varchar(255) DEFAULT NULL,
  `Plot no.(CH18)` varchar(255) DEFAULT NULL, 
  `Area(CH18)` varchar(255) DEFAULT NULL,
  `Lagan(CH18)` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `CHForm11 5`
--
CREATE TABLE `CHForm11 5` (
  `Serial no.` varchar(255) DEFAULT NULL,
  `Khatuni no.` varchar(255) DEFAULT NULL, 
  `Total Lagan` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `CH23 1`
--
CREATE TABLE `CH23 1` (
  `Id` varchar(255) DEFAULT NULL,
  `Serial no.` varchar(255) DEFAULT NULL,
  `Name of holder` varchar(255) DEFAULT NULL,
  `Name of father/husband/guardian` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `CH23 2`
--
CREATE TABLE `CH23 2` (
  `Serial no.` varchar(255) DEFAULT NULL,
  `Sr. no. of CH11` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `CH23 3`
--
CREATE TABLE `CH23 3` (
  `Id` varchar(255) DEFAULT NULL,
  `Serial no.` varchar(255) DEFAULT NULL,
  `Plot no.` varchar(255) DEFAULT NULL,
  `Area of plot` varchar(255) DEFAULT NULL,
  `Area of plot for CH18` varchar(255) DEFAULT NULL,
  `Area of plot in consolidation` varchar(255) DEFAULT NULL,
  `Exchange rate of consolidated area` varchar(255) DEFAULT NULL,
  `Value of consolidated area` varchar(255) DEFAULT NULL,
  `Lagan of inividual plot` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `CH23 4`
--
CREATE TABLE `CH23 4` (
  `Serial no.` varchar(255) DEFAULT NULL,
  `Contribution for public purpose in terms of anna value` varchar(255) DEFAULT NULL,
  `Contribution for public purpose in terms of area` varchar(255) DEFAULT NULL,
  `Reservation lagan` varchar(255) DEFAULT NULL,
  `Amount of compensation` varchar(255) DEFAULT NULL,
  `Net evaluation` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `CH23 5`
--
CREATE TABLE `CH23 5` (
  `Id` varchar(255) DEFAULT NULL,
  `Serial no.` varchar(255) DEFAULT NULL,
  `Land category` varchar(255) DEFAULT NULL,
  `New plot no.` varchar(255) DEFAULT NULL,
  `Area` varchar(255) DEFAULT NULL,
  `Exchange rate` varchar(255) DEFAULT NULL,
  `Net Evaluation of new plot` varchar(255) DEFAULT NULL,
  `New land revenue` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `CH41 1`
--
CREATE TABLE `CH41 1` (
  `New Plot no.` varchar(255) DEFAULT NULL,
  `New Plot area` varchar(255) DEFAULT NULL,
  `Sr. No. of CH45` varchar(255) DEFAULT NULL,
  `Soil Class` varchar(255) DEFAULT NULL,
  `Irrigation Source` varchar(255) DEFAULT NULL,
  `Remark` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `CH41 2`
--
CREATE TABLE `CH41 2` (
  `Id` varchar(255) DEFAULT NULL,
  `New Plot No.` varchar(255) DEFAULT NULL,
  `Old Plot No.` varchar(255) DEFAULT NULL,
  `Old Plot Area` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `CH45 1`
--
CREATE TABLE `CH45 1` (
  `Khatauni no.` varchar(255) DEFAULT NULL,
  `Total area` varchar(255) DEFAULT NULL,
  `Lagan` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `CH45 2`
--
CREATE TABLE `CH45 2` (
  `Id` varchar(255) DEFAULT NULL,
  `Khatauni no.` varchar(255) DEFAULT NULL,
  `Name of holder` varchar(255) DEFAULT NULL,
  `Name of father/husband/guardian` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
-- --------------------------------------------------------
--
-- Table structure for table `CH45 3`
--
CREATE TABLE `CH45 3` (
  `Id` varchar(255) DEFAULT NULL, 
  `Khatauni no.` varchar(255) DEFAULT NULL,
  `Fasli Year` varchar(255) DEFAULT NULL,
  `Khasra/Plot No.` varchar(255) DEFAULT NULL,
  `Plot Area` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
"""