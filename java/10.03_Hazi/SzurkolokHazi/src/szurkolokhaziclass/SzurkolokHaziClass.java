package szurkolokhaziclass;

import java.util.Random;

public class SzurkolokHaziClass {

    public static void main(String[] args) {
        Random rnd = new Random();
        int also = 1, felso = 10;
        int foRobotTipp = rnd.nextInt(felso) + also;
        int kisRobot1 = rnd.nextInt(felso) + also;
        int kisRobot2 = rnd.nextInt(felso) + also;
        int kisRobot3 = rnd.nextInt(felso) + also;
        
        /* TESZTELĂ‰SRE */
        /*foRobotTipp = 7;
        kisRobot1 = 7;
        kisRobot2 = 7;
        kisRobot3 = 7;*/
        /* TESZT VĂ‰GE */
        
        System.out.println("A gondolt szĂˇm: " + foRobotTipp);
        System.out.println("1. robot tippje: " + kisRobot1);
        System.out.println("2. robot tippje: " + kisRobot2);
        System.out.println("3. robot tippje: " + kisRobot3);
        boolean voltTalalat = false;
        String szoveg = "";
        if(foRobotTipp == kisRobot1){
            //System.out.println("Az 1. robot eltatlĂˇlta!");
            szoveg = "Az 1. robot eltatlĂˇlta!\n";
            voltTalalat = true;
        }
        if(foRobotTipp == kisRobot2){
            //System.out.println("A 2. robot eltatlĂˇlta!");
            szoveg = szoveg + "Az 2. robot eltatlĂˇlta!\n";
            voltTalalat = true;
        }
        if(foRobotTipp == kisRobot3){
            //System.out.println("A 3. robot eltatlĂˇlta!");
            szoveg = szoveg + "Az 3. robot eltatlĂˇlta!\n";
            voltTalalat = true;
        }
        
        if(!voltTalalat){
            System.out.println("Egyik robot sem talĂˇlta el");
        }else{
            System.out.println(szoveg);
        }
    }
    
}
