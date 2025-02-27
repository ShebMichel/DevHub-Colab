# FuelWatch AU Project by SPLATPLAYS

A Flask web application that helps users find the closest and cheapest fuel stations in Western Australia using the FuelWatch API. Get real-time fuel prices and find the best deals near you.

## Features

- Search for fuel stations by suburb or address in Western Australia
- Filter by fuel types (ULP, PULP, Diesel, LPG, etc.)
- Display the 30 closest fuel stations to your location
- Show real-time fuel prices and distance information
- Mobile-responsive design for easy use on any device
- Automatic geolocation using OpenStreetMap
- Support for all WA regions

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Web browser (Chrome, Firefox, Safari, etc.)
- Internet connection

## Installation

1. Clone the repository:
```bash
git clone https://github.com/SPLATPLAYS/fuelwatch-app.git
cd fuelwatch-app
```

2. Install required packages:
```bash
pip install flask requests feedparser geopy logging
```

## Usage

1. Start the application:
```bash
python3 main.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Select your fuel type from the dropdown menu
4. Enter your suburb or address (e.g., "Neerigen St, Armadale WA 6112")
5. Click "Search" to find nearby fuel stations

## Supported Fuel Types

- ULP (Unleaded Petrol)
- PULP (Premium Unleaded)
- Diesel
- LPG
- Brand Diesel
- 98 RON
- E85

## API Information

This application uses:
- WA FuelWatch RSS Feed API for real-time fuel prices
- OpenStreetMap's Nominatim for geocoding addresses
- Geopy for distance calculations

## Project Structure

```
fuelwatch-app/
├── main.py              # Main application file
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
├── LICENSE            # MIT License file
└── templates/         # HTML templates
    └── index.html    # Main page template
```

## Configuration

The application uses the following default settings:
- Development server on localhost:5000
- Debug mode enabled for development
- Maximum of 30 stations displayed per search
- Distances calculated in kilometers
- Automatic region detection
- Response caching disabled for real-time prices

## Development

To run the application in development mode with debug logging:

```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
python3 main.py
```

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Data provided by [WA FuelWatch](https://www.fuelwatch.wa.gov.au)
- Geocoding by [OpenStreetMap](https://www.openstreetmap.org)
- Flask web framework
- Python community

## Author

SPLATPLAYS

## Support

For support:
1. Check the [Issues](https://github.com/SPLATPLAYS/fuelwatch-app/issues) page
2. Open a new issue with:
   - Description of the problem
   - Steps to reproduce
   - Expected behavior
   - Screenshots if applicable
