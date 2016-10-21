/////////////////////////////////////////////////////////////////
// Created By Alex Steel
// Program #4 - Hunt the Wumbus
// February 28th, 2014
// Program Description - You are a mighty warrior, and armed with 
//your trusty bow and 3 arrows, you enter The Caves in search of the 
//mighty Wumpus. If you shoot the Wumpus, you are victorious and the 
//masses will praise you, but if you stumble upon the Wumpus unawares, 
//it will eat you! Also, beware of the webs of the giant poisonous spiders 
//and the bottomless pits!
/////////////////////////////////////////////////////////////////

import java.io.*;
import java.util.*;

public class Caves
{
	// creating data markers
	int roomnumber, exit1, exit2, exit3;
	String warning;

	// initializing the data markers
	public Caves()
	{
		roomnumber=exit1=exit2=exit3=0;
		warning="";
	}
	public Caves(String w, int rn, int e1, int e2, int e3)
	{
		warning=w;
		roomnumber=rn;
		exit1=e1;
		exit2=e2;
		exit3=e3;
	}
	String extra;
	public Caves(Scanner cin)
	{
		roomnumber=cin.nextInt();
		exit1=cin.nextInt();
		exit2=cin.nextInt();
		exit3=cin.nextInt();
		String extra=cin.nextLine();
		warning=cin.nextLine();
	}
	
	public String toString()
	{
		return roomnumber + " " + exit1 + " " + exit2 + " " + exit3 + " " + warning;
	}
	
	public int getRoomnumber()	{return roomnumber;}
	public int getExit1()	{return exit1;}
	public int getExit2()	{return exit2;}
	public int getExit3()	{return exit3;}
	public String getWarning() {return warning;}
	
	
}

