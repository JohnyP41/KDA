using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KDA1
{
    class Program
    {
        static void Main(string[] args)
        {
            float k = int.Parse(Console.ReadLine());

            string line = Console.ReadLine();
            string[] tokens = line.Split(' ');
            float[] numbers = Array.ConvertAll(tokens, float.Parse);

            float[] number_skal = new float[numbers.Length];

            float max = numbers.Max();
            float min = numbers.Min();

            float super_max = Math.Max(Math.Abs(min), Math.Abs(max));

            float s = 2 / (k+1);
            float t = 0;

            List<float> range_x = new List<float>();
            List<float> range_y = new List<float>();
            for (int x = 0; x<=k; x++)
            {
                range_x.Add(-1 + t);
                range_y.Add(-1 + t + s);
                t += s;
            }

            List<float> output = new List<float>();
            float z = 0;
            for(int x=0;x<numbers.Length;x++)
            {
                z = 0;
                for(int j=0;j<range_x.Count; j++)
                {
                    if (x >= range_x[x] && x < range_y[x]) output.Add(z);  

                        z++;
                }
            }

            float delta = max - min;
            int i = 0;
            for(int x=0;x<=k;x++)
            {
                Console.WriteLine("[x= " + range_x[x] + " y= " + range_y[x] + "]\t");
            }

            foreach (float x in numbers)
            {
                number_skal[i] = x / super_max;
                i++;
            }

            for(int j=0; j<number_skal.Length;j++)
            {
                Console.WriteLine(number_skal[j]);
            }

            Console.WriteLine("max= " + max + " min=" + min);
            Console.ReadKey();
        }
    }
}