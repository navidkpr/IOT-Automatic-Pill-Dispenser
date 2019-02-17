package com.MakeUofT.PillDispende;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
 
import com.itextpdf.text.Document;
import com.itextpdf.text.Paragraph;
import com.itextpdf.text.pdf.PdfWriter;
/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        Document document = new Document();
      try
      {
         PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("HelloWorld.pdf"));
         document.open();
         document.add(new Paragraph("A Hello World PDF document."));
         document.close();
         writer.close();
      } catch (Exception e){
          e.printStackTrace();
      }
    }
}
