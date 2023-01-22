using System;

namespace ConsoleTesting2
{
    class Program
    {
        static void Main(string[] args)
        {
            
            int testVar = 9;
            int testInt = 10;
            float speedFloat = 22_000.5f;
            double speedDouble = 33_000.5;
            //double speedDoubleWithD = 33_000.5D;
            decimal speedDecimal = 44_000.5m;
            bool isClosed = false;
            char character = '.';
            string name = "Your Name";
            int age = 30;
            double height = 9.3;

            Console.WriteLine( testInt + testVar);
            Console.WriteLine(speedFloat);
            Console.WriteLine();
            Console.WriteLine(speedDouble);
            Console.WriteLine(speedDecimal);
            Console.WriteLine();
            Console.WriteLine(isClosed);
            Console.WriteLine(character);
            Console.WriteLine("Name: " + name);
            Console.WriteLine("Age: " + age);
            Console.WriteLine("Height: " + height);
            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine("Name: " + name + "\n" + "Age: " + age + "\n" + "Height: " + height);
            Console.WriteLine("Name: {0} \nAge: {1} \nHeight: {2}", name, age, height); // Composite formatting
            Console.WriteLine();
            Console.WriteLine($"Name: {name} \nAge: {age} \nHeight: {height}"); // String Interpolation
            Console.WriteLine();
            Console.WriteLine("Total: " + (speedDouble + height));

            const int maxHealth = 100;
            Console.WriteLine(maxHealth);
            //Console.ReadKey();
        }
    }
}

