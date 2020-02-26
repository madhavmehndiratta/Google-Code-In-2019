class Nasa{
    constructor(){
        this.api = 'soJCo1NCoSLlWaVuLXdrh2HU0JySPggUKZ7ROMhY';
    }

    async getData( date ){
	    console.log(date);
        const getResponse = await fetch(`https://api.nasa.gov/planetary/apod?start_date=${date}&end_date=${date}&api_key=GdWau7tPdPNkucMLX5xgTIDTL9cELo21FGPAdQmP`);
	   var getData = await getResponse.json();
	   
	   return getData[ 0 ];
    }
}