import java.util.Scanner;
public class App {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        String Judul, Author, Penerbit;
        int id, Tahun;
            System.out.println("===========================================================");
            System.out.println("\tSelamat Datang Di Perpustakaan Sederhana");
            System.out.println("===========================================================");
            System.out.println("Silahkan Masukan Kriteria Buku\n");
            System.out.print("Masukan Id:");
            id = scan.nextInt();
            scan.nextLine();
            System.out.print("Judul : ");
            Judul = scan.nextLine();
            System.out.print("Author : ");
            Author = scan.nextLine();
            System.out.print("Penerbit : ");
            Penerbit = scan.nextLine();
            System.out.print("Tahun : ");
            Tahun = scan.nextInt();
            System.out.println("\n\n");
    // isi
    System.out.println("===========================================================");
    System.out.println("\t\tBuku yang telah ditambahkan");
    System.out.println("===========================================================");
    System.out.println("Id : " + id);
    System.out.println("Judul : " + Judul);
    System.out.println("Auhtor : " + Author);
    System.out.println("Penerbit : " + Penerbit);
    System.out.println("Tahun : " + Tahun);
    scan.close();    
    }
};
