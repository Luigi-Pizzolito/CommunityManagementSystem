// Helper function to aggregate stations by hour
function aggregateStationsByHour(timestamps) {
    var stationsByHour = {};

    timestamps.forEach(timestamp => {
        var hour = timestamp.getHours();
        stationsByHour[hour] = (stationsByHour[hour] || 0) + 1;
    });

    return stationsByHour;
}

function loadJSON(filename, callback) {
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', filename, true);
    xobj.onreadystatechange = function () {
        if (xobj.readyState == 4 && xobj.status == "200") {
            callback(xobj.responseText);
        }
    };
    xobj.send(null);
}

function createGraphs() {
    // Garbage Station Data Analysis and Graph Creation
    loadJSON('./json/fake_garbage_station_data.json', function(response) {
        var garbageStationData = JSON.parse(response);

        // Extracting timestamps and statuses
        var timestamps = garbageStationData.map(item => new Date(item.timestamp));
        var statuses = garbageStationData.map(item => item.status);

        // Grouping stations by status (Full/Normal/Empty)
        var fullStations = timestamps.filter((_, index) => statuses[index] === 'Full');
        var normalStations = timestamps.filter((_, index) => statuses[index] === 'Normal');
        var emptyStations = timestamps.filter((_, index) => statuses[index] === 'Empty');

        // Aggregating stations by hour
        var fullStationsByHour = aggregateStationsByHour(fullStations);
        var normalStationsByHour = aggregateStationsByHour(normalStations);
        var emptyStationsByHour = aggregateStationsByHour(emptyStations);

        // Plotting the graph for Garbage Stations
        var fullTrace = {
            x: Array.from({ length: 24 }, (_, i) => i), // Time interval 0 to 24 hours
            y: Array.from({ length: 24 }, (_, i) => fullStationsByHour[i] || 0),
            type: 'bar',
            name: 'Full Stations'
        };

        var normalTrace = {
            x: Array.from({ length: 24 }, (_, i) => i), // Time interval 0 to 24 hours
            y: Array.from({ length: 24 }, (_, i) => normalStationsByHour[i] || 0),
            type: 'bar',
            name: 'Normal Stations'
        };

        var emptyTrace = {
            x: Array.from({ length: 24 }, (_, i) => i), // Time interval 0 to 24 hours
            y: Array.from({ length: 24 }, (_, i) => emptyStationsByHour[i] || 0),
            type: 'bar',
            name: 'Empty Stations'
        };

        var layout = {
            title: 'Garbage Stations Status by Hour of the Day',
            xaxis: { title: 'Hour of the Day', range: [0, 24] }, // Setting the x-axis range to 0-24 hours
            yaxis: { title: 'Number of Stations' }
        };

        Plotly.newPlot('garbageStationGraph', [fullTrace, normalTrace, emptyTrace], layout);
    });


    // Similar Analysis and Graph Creation for other datasets
    // Attention Data
    // Parked Cars Data
    // Patrol Data
    // Attention Data Analysis and Graph Creation
    loadJSON('./json/fake_attention_data.json', function(response) {
        var attentionData = JSON.parse(response);

        // Extracting emergency types
        var emergencyTypes = attentionData.map(item => item.emergencyType);

        // Counting occurrences of emergency types
        var emergencyTypeCount = {};
        emergencyTypes.forEach(type => {
            emergencyTypeCount[type] = (emergencyTypeCount[type] || 0) + 1;
        });

        // Creating data for the pie chart
        var pieData = {
            values: Object.values(emergencyTypeCount),
            labels: Object.keys(emergencyTypeCount),
            type: 'pie'
        };

        var pieLayout = {
            title: 'Emergency Type Distribution'
        };

        Plotly.newPlot('attentionPieChart', [pieData], pieLayout);
    });

    // Parked Cars Data Analysis and Graph Creation
    loadJSON('./json/fake_parked_cars_data.json', function(response) {
        var parkedCarsData = JSON.parse(response);

        // Extracting timestamps and number of cars
        var timestamps = parkedCarsData.map(item => new Date(item.timestamp));
        var carNumbers = parkedCarsData.map(item => item.numberOfCars);

        // Grouping cars by hour
        var carsByHour = {};
        timestamps.forEach((timestamp, index) => {
            var hour = timestamp.getHours();
            carsByHour[hour] = (carsByHour[hour] || 0) + carNumbers[index];
        });

        // Plotting the graph for Parked Cars
        var carTrace = {
            x: Object.keys(carsByHour),
            y: Object.values(carsByHour),
            type: 'bar',
            name: 'Number of Cars'
        };

        var carLayout = {
            title: 'Parked Cars by Hour of the Day',
            xaxis: { title: 'Hour of the Day' },
            yaxis: { title: 'Number of Cars' }
        };

        Plotly.newPlot('parkedCarsGraph', [carTrace], carLayout);
    });

        // Patrol Data Analysis and Graph Creation
    loadJSON('./json/fake_patrol_data.json', function(response) {
        var patrolData = JSON.parse(response);

        // Extracting timestamps
        var timestamps = patrolData.map(item => new Date(item.timestamp));

        // Grouping patrols by hour
        var patrolsByHour = aggregateStationsByHour(timestamps);

        // Plotting the graph for Patrols
        var patrolTrace = {
            x: Object.keys(patrolsByHour),
            y: Object.values(patrolsByHour),
            type: 'bar',
            name: 'Number of Patrols'
        };

        var patrolLayout = {
            title: 'Patrols by Hour of the Day',
            xaxis: { title: 'Hour of the Day' },
            yaxis: { title: 'Number of Patrols' }
        };

        Plotly.newPlot('patrolGraph', [patrolTrace], patrolLayout);
    });

    

    loadJSON('./json/fake_census_data.json', function(response) {
        var censusData = JSON.parse(response);

        // Filter residents and non-residents
        var residents = censusData.filter(person => person.permanentResidency === 'Yes');
        var nonResidents = censusData.filter(person => person.permanentResidency === 'No');

        // Count employment status for residents
        var employedResidents = residents.filter(person => person.employmentStatus === 'Employed').length;
        var unemployedResidents = residents.filter(person => person.employmentStatus === 'Unemployed').length;
        var otherResidents = residents.length - employedResidents - unemployedResidents;

        // Count employment status for non-residents
        var employedNonResidents = nonResidents.filter(person => person.employmentStatus === 'Employed').length;
        var unemployedNonResidents = nonResidents.filter(person => person.employmentStatus === 'Unemployed').length;
        var otherNonResidents = nonResidents.length - employedNonResidents - unemployedNonResidents;

        // Plotting the graph for Census Data
        var trace1 = {
            x: ['Employed', 'Unemployed', 'Other'],
            y: [employedResidents, unemployedResidents, otherResidents],
            type: 'bar',
            name: 'Residents'
        };

        var trace2 = {
            x: ['Employed', 'Unemployed', 'Other'],
            y: [employedNonResidents, unemployedNonResidents, otherNonResidents],
            type: 'bar',
            name: 'Non-Residents'
        };

        var layout = {
            title: 'Employment Status Comparison',
            xaxis: { title: 'Employment Status' },
            yaxis: { title: 'Number of Individuals' }
        };

        Plotly.newPlot('censusGraph', [trace1, trace2], layout);
    });

}



    

createGraphs();
