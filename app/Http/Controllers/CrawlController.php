<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;
use Illuminate\Support\Facades\Http;

class CrawlController extends Controller
{
    public function Scrape(Request $request)
    {

    
        //setting waktu eksekusi maksimal snscrape
        ini_set('max_execution_time', 0);
        //Eksekusi atau menjalankan script snscrape py
        $output = shell_exec('python C:\xampp\htdocs\sna-app\app\Http\Controllers\test.py "'.$request->katakunci1.'" "'.$request->katakunci2.'" "'.$request->katakunci3.'" "'.$request->katakunci4.'" "'.$request->startdate.'" "'.$request->enddate.'"');
        echo($output);
        exit();
        return $this->Crawl($output);
    
    }

    public function Crawl($output)
    {
        
        #$response = Http::get('localhost:3000/unpreprocess')->json();
        #dd($response);

        ini_set('max_execution_time', 0);
      
        //Eksekusi atau menjalankan script snscrape py
        $hasil = shell_exec('python C:\xampp\htdocs\sna-app\app\Http\Controllers\crawl.py "'.$output.'" "');
        echo($hasil);  
      



    }


    public function GetApi($output)
    {
        echo($output);
        exit();
        #$response = Http::get('localhost:3000/unpreprocess')->json();
        #dd($response);

        ini_set('max_execution_time', 0);
      
        //Eksekusi atau menjalankan script snscrape py
        $hasil = shell_exec('python C:\xampp\htdocs\sna-app\app\Http\Controllers\crawl.py "'.$output.'" "');
        
      



    }


    public function visualize()
    {
        //nama file yg di create
        $file_name = '\uy.py';
        //route direktori file
        $realpath = 'C:\xampp\htdocs\sna-app\public'.$file_name;
        dd($realpath);
        ini_set('max_execution_time', 0);
        
        //Eksekusi atau menjalankan script snscrape py
       //$output = shell_exec($realpath);
        $output = shell_exec("python --version");
       

    }

    public function Sna()
    {
          
              //setting waktu eksekusi maksimal snscrape
              ini_set('max_execution_time', 0);
       
              //Eksekusi atau menjalankan script snscrape py
               $output = shell_exec('python C:\xampp\htdocs\sna-app\public\uy.py');
              
              echo($output);

    }




}
?>