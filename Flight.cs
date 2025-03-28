using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AirTrafficControl
{
    public class Flight
    {
        public string FlightID { get; set; }
        public DateTime Time { get; set; }  
        public int Altitude { get; set; }
        public int Speed { get; set; }

        public Flight(string id, DateTime time, int altitude, int speed)
        {
            FlightID = id;
            Time = time;
            Altitude = altitude;
            Speed = speed;
        }

        public override string ToString()
        {
            return $"Flight {FlightID} | Time: {Time} | Altitude: {Altitude} | Speed: {Speed}";
        }
    }
}

