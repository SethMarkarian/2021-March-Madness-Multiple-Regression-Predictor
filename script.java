public class script {
    
    public static void main(String[] args) {

        //4
        // String[] arr = {"i", "j", "k", "l"};
        // int count = 0;
        // for(int a = 0; a != arr.length; a++) {
        //     for(int b = 0 ; b != arr.length; b++) {
        //         for(int c = 0; c != arr.length; c++) {
        //             for(int d = 0; d != arr.length; d++) {
        //                 if(a != b && a != c && a != d && b != c && b != d && c != d) {
        //                     System.out.println("completed_combinations.append(" + arr[a] + " + " + arr[b] + " + " + arr[c] + " + " + arr[d] + ")");
        //                     count++;
        //                 }
        //             }
        //         }
        //     }
        // }
        // System.out.println(count);

        //5
        // String[] arr = {"i", "j", "k", "l", "m"};
        // int count = 0;
        // for(int a = 0; a != arr.length; a++) {
        //     for(int b = 0 ; b != arr.length; b++) {
        //         for(int c = 0; c != arr.length; c++) {
        //             for(int d = 0; d != arr.length; d++) {
        //                 for(int e = 0; e != arr.length; e++) {
        //                     if(a != b && a != c && a != d && a != e && b != c && b != d && b != e && c != d && c != e && d != e) {
        //                         System.out.println("completed_combinations.append(" + arr[a] + " + " + arr[b] + " + " + arr[c] + " + " + arr[d] + " + " + arr[e] + ")");
        //                         count++;
        //                     }
        //                 }
        //             }
        //         }
        //     }
        // }
        // System.out.println(count);

        //5
        String[] arr = {"i", "j", "k", "l", "m", "n"};
        int count = 0;
        for(int a = 0; a != arr.length; a++) {
            for(int b = 0 ; b != arr.length; b++) {
                for(int c = 0; c != arr.length; c++) {
                    for(int d = 0; d != arr.length; d++) {
                        for(int e = 0; e != arr.length; e++) {
                            for(int f = 0; f != arr.length; f++) {
                                if(a != b && a != c && a != d && a != e && a != f && b != c && b != d && b != e && b != f && c != d && c != e && c != f && d != e && d != f && e != f) {
                                    System.out.println("completed_combinations.append(" + arr[a] + " + " + arr[b] + " + " + arr[c] + " + " + arr[d] + " + " + arr[e] + " + " + arr[f] + ")");
                                    count++;
                                }
                            }
                        }
                    }
                }
            }
        }
        System.out.println(count);
    }
}
