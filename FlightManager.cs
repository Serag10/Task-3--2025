using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AirTrafficControl
{
    public class FlightManager
    {
        private List<Flight> flights;

        public FlightManager()
        {
            flights = new List<Flight>()
            {
                new Flight("A1", new DateTime(2025, 3, 25, 14, 30, 0), 30000, 500),
                new Flight("BG2", new DateTime(2025, 3, 25, 10, 15, 0), 32000, 550),
                new Flight("CCA5", new DateTime(2025, 3, 25, 12, 45, 0), 28000, 520),
                new Flight("ABC6", new DateTime(2025, 3, 25, 16, 0, 0), 31000, 510),
                new Flight("RTE55", new DateTime(2025, 3, 25, 9, 0, 0), 29000, 530)
            };

        }
        public void SortFlights()
        {
            Console.WriteLine("Before Sorting:");
            foreach (var flight in flights) 
            { 
                Console.WriteLine($"\n{flight}");
            }
            FlightSorter.MergeSort(flights, 0, flights.Count - 1);

            Console.WriteLine("\n\n\nAfter Sorting (By Time):");
            foreach (var flight in flights)
            {
                Console.WriteLine($"\n{flight}");
            }
        }

    }
}
