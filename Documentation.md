# Current F1 Drivers
10PSE Task 1

## Determining Specifications
### Functional Specifications
**User Requirements**  
The user needs to be able to:  
1. Search for a F1 driver by entering their name
2. Filter drivers based on team or nationality
4. View their list

**Inputs and Outputs**  
The system will accept inputs including:
1. The name of the drivers
2. The filter - team or nationality
2. The name of the team or country
4. The name of the driver they either want to add or remove from their list

and the outputs would be:  
1. The information on the specific driver
2. The drivers in that team
3. The drivers of that nationality
4. Their list

**Core Features**  
The program needs to clearly produce the requested information from the API URL that the user has asked for. It should search and filter data based on driver name, team name and nationality and handle incorrect or missing user inputs. 

**User Interaction**  
The program will be used through a command-line interface and I will create a README.md file. The README.md file will provide a:
1. Description of my program
2. Setup Instructions (txt file)
3. How to run the program
4. Examples of valid inputs
5. Dependancies

**Error Handling**
My system must handle unidentified wrong inputs or errors in the API URL. This includes unexpected inputs of driver or team names, errors or missing fields in the API and APU connection failures. 

### Non-Functional Specifications
**Performance**    
My program should respond quickly enough so that the users dont feel the system lagging. The responses should be efficient and be kept under a second at best to maintain user engagement. 

**Useability/Accessibility**    
The program should have clear prompts asking users exactly what they need to type, consistent formatting with clearn readable outputs with spacing, indentation and lables and also helpful error messages to show when the wrong inputs were put in. 
(users whouldnt need to type exact names, shortcuts)

**Reliability**  
Potential issues may include API downtime, missing data, incorrect user inputs and duplicated data. The program shuld allow the users to try again, show a error message, and filter out unneeded extra information. 

## Requirements
### Functional Requirements
**Data Retrieval**  
The user must be able to view information about specific F1 drivers, team or country thier own lists created through the program.

**User Interface**  
There has to be a way for users to search or filter information, a way to trigger outputs like specific inputs, a clear display of results and a way to manage their personal lists. 

**Data Display**  
The user needs to obtain information such as thier name, age, nationality and their current team. Their should also be seperate lists based on teams or nationalities of the drivers and the user's personal driver list.

### Non-Functional Requirements
**Performance**  
The system needs to respond quickly and handle user inputs without any delays. Searching for a driver, filtering by team or nationality or updating the user's list should feel immediate so that the experience remains smooth. It should handle multiple searches without slowing down and manage the full API without errors or lags.

**Reliability**  
The systems needs to be dependable so users trust the information provided. Driver data, team lists and nationality filters must always produce accurate and consistent results and make sure to update correctly every time when the list is changed. It should also make sure the system does not crash, lose data or produce inconsistent outputs depending on the order of actions.

**Usability and Accessibility**  
The system needs to be easy and clear to navigate so users can find waht they need without confsion. Clear labels and simple menus should help users understand how to work the program and the interface hsould avoid clutter and present the results in a clean, readable format. Instructions on what to input should be brief and direct. The README.md file will present step by step instructions for users on how to use and access the system. 

## Use Cases
### Use Case 1 - Search for a F1 driver by entering their name
**Actor**  
User

**Preconditions**  
- The F1 API is reachable
- The requirements.txt has been installed

**Main Flow**  
1. User chooses option no.1
2. User enters a driver's name (e.g. "Charles Leclerc")
3. System retrieves all driver data from the API
4. System searches for a matching driver
5. System displays the driver's details

**Alternative Flows**
- Driver not found : System displays 'Driver not found. Please try again.'
- API downtime : System displays "Unable to retrieve driver data. Please try again after a little while."

### Use Case 2 - Filter drivers based on team or nationality
**Actor**  
User

**Preconditions**  
- The F1 API is reachable
- The requirements.txt has been installed

**Main Flow**  
1. User chooses option no.2
2.  User choose a filter
        * Country - User inputs the name of a country
        * Team - User inputs the name of a team

**Alternative Flows**
- Team not found : System displays 'Team not found. Please try again.'
- Country not found : System displays 'Country no found. Please try again.'
- API downtime : System displays "Unable to retrieve team data. Please try again after a little while."

### Use Case 3 - Their list
**Actor**  
User

**Preconditions**  
- The F1 API is reachable
- The requirements.txt has been installed

**Main Flow**  
1. User chooses option no.3
2. User chooses out of viewing, adding or removing from their list  
        * Viewing - Program outputs the list  
        * Adding - User inputs the name of the driver they want to add to their list  
        * Removing - User inputs the name of the driver they want to remove from their list

**Alternative Flows**
- Nothing to view : System displays 'No drivers found in your list. Please add a driver before trying again.'
- Driver not found : System displays 'Driver not found. Please try again.'
- Driver not found in list : System displays 'Driver not found in list. Please try again.'
- API downtime : System displays "Unable to retrieve data. Please try again after a little while."

## Pseudocode
## Flowchart

## Structure Chart
![](./images/Structure_Chart.jpeg)

## IPO - input, process, output
## Gantt Chart  - Development  
Start  
![](./images/)
End
![](./images/)

## Data Dictionary
| Field | Datatype | Format for display | Description | Example | Validation |
|----------|--------------|------------------------|------------------|-------------|----------------|
| Driver Name | string | XX...XX  | The full name of the F1 driver the user searches for or adds/removes from their list | Charles Leclerc | Must contain letters and spaces only; cannot be empty |
| Team | string | XX...XX | The team used when filtering drivers | Ferrari | Must match a valid team name from the API |
| Country | string | XX...XX | The country used when filtering drivers | Monaco | Must contain letters only; must match API data |
| Filter Type | string | XX...XX | Determines how the system filters drivers | team | Must be exactly “team” or “nationality” |
| Filter Value | string | XX...XX | The team or nationality entered by the user | Ferrari | Must match API data |
| List Action | string | XX...XX | The action the user chooses for their list | add | Must be one of the three valid options |
| User List | list | XX...XX | The list of drivers saved by the user | Charles Leclerc | No duplicates; each entry must be a valid driver |
| Error Message | string | XX...XX | Message displayed when an input or API issue occurs | Driver not found. | Must clearly describe the issue |


## Design
## Development
## Integration
## Testing and Debugging
### Student feeback - Arisa Komatsu
### Student feedback - Isabella Usacheva
## Maintenance
