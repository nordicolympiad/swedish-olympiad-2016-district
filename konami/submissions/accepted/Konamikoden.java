import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;
public class Konamikoden {
  private static class SubS {
    int k = 0;
    int i = 1;
    public SubS(){
    }
  }
  public static void main(String args[]) {
    String code = "UUNNVHVHBA";
    Scanner sc = new Scanner(System.in);
    String in = sc.next();
    int mink = Integer.MAX_VALUE;
    LinkedList<SubS> strs = new LinkedList<SubS>();
    for(int j = 0; j<in.length(); j++) {
      int lasti = 0;
      if(in.charAt(j) == code.charAt(0))
        strs.addFirst(new SubS());
      Iterator<SubS> itr = strs.iterator();
      while(itr.hasNext()){
        SubS now = itr.next();
        if(code.charAt(now.i) == in.charAt(j)) 
          now.i++;
        else
          now.k++;
        if(now.i == 9) {
          if(now.k<mink)
            mink = now.k;
          itr.remove();
        }
        if(now.i == lasti) {
          itr.remove();
        }
        lasti = now.i;
      }
    }
    System.out.println(mink);
  }
}

