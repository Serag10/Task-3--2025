using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AirTrafficControl
{
    public class FlightSorter
    {
        public static void MergeSort(List<Flight> flights, int left, int right)
        {
            if (left < right)
            {
                int mid = (left + right) / 2;

                MergeSort(flights, left, mid);
                MergeSort(flights, mid + 1, right);

                Merge(flights, left, mid, right);
            }
        }

        private static void Merge(List<Flight> flights, int left, int mid, int right)
        {
            List<Flight> leftList = flights.GetRange(left, mid - left + 1);
            List<Flight> rightList = flights.GetRange(mid + 1, right - mid);

            int i = 0, j = 0, k = left;

            while (i < leftList.Count && j < rightList.Count)
            {
                int timeComparison = leftList[i].Time.CompareTo(rightList[j].Time);

                if (timeComparison < 0 || (timeComparison == 0 && leftList[i].Speed < rightList[j].Speed))
                {
                    flights[k] = leftList[i];
                    i++;
                }
                else
                {
                    flights[k] = rightList[j];
                    j++;
                }
                k++;
            }

            while (i < leftList.Count)
            {
                flights[k] = leftList[i];
                i++;
                k++;
            }

            while (j < rightList.Count)
            {
                flights[k] = rightList[j];
                j++;
                k++;
            }
        }
    }
}

