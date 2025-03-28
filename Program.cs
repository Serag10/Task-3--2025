using System;

namespace AirTrafficControl
{
    class Program
    {
        static void Main()
        {

            Console.WriteLine("Name: Hazem Ibrahim Abdel-Hamed Mohamed Aldriny | Section:3");
            Console.WriteLine("\nTraget:" +
                              "implementing Merge Sort to prioritize flights based on scheduling needs.\n" +
                              "Primary Criterion: Sorting by Time (earliest flights first).\n" +
                              "Secondary Criterion: If times are equal, sorting by Speed (lower speeds first for smoother scheduling).\n"
                              ); 
            FlightManager manager = new FlightManager();
            manager.SortFlights();

            Console.ReadLine();
        }
    }
}
