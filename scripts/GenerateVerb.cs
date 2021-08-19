using System;
using System.Collections.Generic;
using Gramadan;
using System.IO;
using System.Xml;
using System.Xml.Linq;

namespace Tester
{
	class Program
	{
		static void Main(string[] args)
		{
			PrinterNeid printer=new PrinterNeid(false);
			XmlDocument doc = new XmlDocument();
			doc.Load("aimsigh_verb.xml");
			Verb verb = new Verb(doc);
			StreamWriter writer = new StreamWriter("aimsigh_print.xml");
			writer.WriteLine(printer.printVerbXml(verb));
			writer.Close();
		}
	}
}
