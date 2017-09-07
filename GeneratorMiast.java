import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Vector;
import java.io.PrintWriter;

class Miasto
{
	public String nazwa;
	public double szerokoscGeo;
	public double dlugoscGeo;
	
	Miasto(String n, double s, double d)
	{
		this.nazwa = n;
		this.szerokoscGeo = s;
		this.dlugoscGeo = d;
	}
}

public class GeneratorMiast
{	
	public static Vector<Miasto> listaMiast = new Vector<>();
	public static HashMap<String, String> paryMiast;
	public static Vector<String> duplikaty = new Vector<>();
	public static FileOutputStream fos;
	public static FileOutputStream fos2;
	public static int i,j;
	public static int KROK;
	
	public void ustawKrok(int a)
	{
		KROK = a;
	}
	
	public String getNazwa(String wiersz)
	{
		int i;
		String wierszLokalny = "";
		char[] array;
		String liczba = "";
		
		wierszLokalny = wiersz.substring(0, 23);
		array = wierszLokalny.toCharArray();
		
		for(i = array.length-1; i >=0; i--)
			if(array[i] != ' ') break;
		
		wierszLokalny = wiersz.substring(0, i+1);
		return wierszLokalny;
	}
	
	public double getDlugoscGeo(String wiersz)
	{
		String wierszLokalny = "";
		char[] array;
		String stopnie = "";
		String minuty = "";
		
		wierszLokalny = wiersz.substring(wiersz.length()-22, wiersz.length()-15);
		
		array = wierszLokalny.toCharArray();
		stopnie = array[0] + "" + array[1];
		minuty =  array[3] + "" + array[4];

		double stopnieDD = Double.parseDouble(stopnie);
		double minutyDD = Double.parseDouble(minuty);
		return stopnieDD + minutyDD/60.;
	}
	
	public double getSzerokoscGeo(String wiersz)
	{
		String wierszLokalny = "";
		char[] array;
		String stopnie = "";
		String minuty = "";
		
		wierszLokalny = wiersz.substring(wiersz.length()-7, wiersz.length());
		
		array = wierszLokalny.toCharArray();
		stopnie = array[0] + "" + array[1];
		minuty =  array[3] + "" + array[4];

		double stopnieDD = Double.parseDouble(stopnie);
		double minutyDD = Double.parseDouble(minuty);
		return stopnieDD + minutyDD/60.;
	}
	
	public void wczytajListeMiast()
	{
		String miasto = "";	
		try 
		{
			BufferedReader br = new BufferedReader(new FileReader(new File("miasta_wspolrzedne.txt")));
			//PrintWriter writer = new PrintWriter("miasta_wspolrzedne_dziesietnie.txt", "UTF-8");
			
			while((miasto = br.readLine()) != null)
			{
				if(miasto.equals("")) continue;
				else if(duplikaty.contains(getNazwa(miasto))) continue;
				else if(getDlugoscGeo(miasto) > 24.00) continue; // wyrzucamy miasta nie polskie
				else if(getDlugoscGeo(miasto) > 23.10 && getSzerokoscGeo(miasto) < 50.00) continue; // wyrzucamy miasta nie polskie
				else
				{
					Miasto city = new Miasto(getNazwa(miasto), getSzerokoscGeo(miasto), getDlugoscGeo(miasto));
					//writer.println(String.format("%.2f", getDlugoscGeo(miasto)).replace(',','.') + '\t' + String.format("%.2f", getSzerokoscGeo(miasto)).replace(',','.'));
					listaMiast.add(city);
					duplikaty.add(city.nazwa);
				}
			}		

			br.close();
			//writer.close();
		} 
		catch (FileNotFoundException e) 
		{
			e.printStackTrace();
		}
		catch (IOException e) 
		{
			e.printStackTrace();
		}
	}
	
	public String obliczDystans(Miasto a, Miasto b)
	{
		Double dystans = Math.sqrt(Math.pow(Math.cos((Math.PI*a.dlugoscGeo)/180.0)*(b.szerokoscGeo-a.szerokoscGeo), 2.0) + Math.pow(b.dlugoscGeo-a.dlugoscGeo, 2.0))*Math.PI*(12756.274/360.0);
		return String.format("%.2f", dystans);
	}
	
	public void generujMape()
	{	
		String aktualniePrzegladaneMiasto = "";
		String dystans = "";
		String wynikowy = "";
		String miasto = "";
		Double postep = 0.0;
		
		if(KROK < 1) { System.out.println("Wartosć kroku nie może być < 1!"); return; }
		System.out.println("Postęp generowania danych:");
		for(i = 0; i < listaMiast.size(); i += KROK)
		{
			postep = (double)i/listaMiast.size();
			System.out.print(String.format("%.2f" ,postep*100.) + "%\r");
			try 
			{
				aktualniePrzegladaneMiasto = listaMiast.get(i).nazwa;
				for(j = 0; j < listaMiast.size(); j += KROK)
				{
					miasto = listaMiast.get(j).nazwa;
					
					if(aktualniePrzegladaneMiasto.equals(miasto)) continue;
					else if(paryMiast.containsValue(miasto)) continue;
					
					paryMiast.put(miasto, aktualniePrzegladaneMiasto);
					
					dystans = obliczDystans(listaMiast.get(i), listaMiast.get(j));
	
				    wynikowy = aktualniePrzegladaneMiasto + "  " + miasto + "  " + dystans + "\n";
				    fos.write(wynikowy.getBytes());
				}
				fos2.write((listaMiast.get(i).nazwa + ";" + String.format("%.2f", listaMiast.get(i).szerokoscGeo).replace(',','.') + ";" + String.format("%.2f", listaMiast.get(i).dlugoscGeo).replace(',','.') + "\n").getBytes());
			}
			catch (IOException e) 
			{
				e.printStackTrace();
			}
		}
		System.out.println("Zakończono!");
	}
	
	public static void main(String[] args)
	{
		GeneratorMiast miasta = new GeneratorMiast();
		paryMiast = new HashMap<>();
		miasta.wczytajListeMiast();
		miasta.ustawKrok(Integer.parseInt(args[0]));
		
		// plik wynikowy
		new File("wygenerowaneDane").mkdir();
		File dane = new File("./wygenerowaneDane/lista_krawedzi_" + KROK + ".txt");
		File lista = new File("./wygenerowaneDane/lista_miast_" + KROK + ".txt");
		try 
		{
			dane.createNewFile();
			lista.createNewFile();
			
			fos = new FileOutputStream(dane);
			fos2 = new FileOutputStream(lista);
			
			miasta.generujMape();
				
		} 
		catch (IOException e) 
		{
			e.printStackTrace();
		}
	}
}
