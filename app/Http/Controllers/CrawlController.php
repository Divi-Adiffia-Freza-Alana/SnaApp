<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\unfilter;
use App\Models\sna;
use Illuminate\Support\Facades\DB;


class CrawlController extends Controller
{
    public function index()
    {

        //$datatable = unfilter::all();
       
        $datatable = DB::table('unfilter')->where('Followers', '>=', 100 )->where('Reply','!=','null')->get();
        return view('home',['datatablelist'=> $datatable]);
       
 
    } 
    public function result()
    {
 
        //$datatable = unfilter::all();
       
        $datatable = DB::table('sna')->get();
        return view('result',['datatablelist'=> $datatable]);
       
 
    }
    public function sna()
    {

        //$datatable = unfilter::all();


       
        $datatable = DB::table('unfilter')->select('Username','Reply')->where('Followers', '>=', 100 )->where('Reply','!=','null')->get();
        //dd($datatable);
        $bit = base64_encode($datatable);
        
        $bot = json_encode($bit,true);

        //setting waktu eksekusi maksimal snscrape
        ini_set('max_execution_time', 0); 
        //Eksekusi atau menjalankan script snscrape py
        $output = shell_exec('python C:\xampp\htdocs\sna-app\app\Http\Controllers\sna.py "'.$bot.'"');
        $var = json_decode($output, TRUE);
        $data=$var['Data'];
        
        sna::truncate();


        foreach($data as $datas) {
            sna::create([
                'Username' => $datas['Username'],
                'Nilai' => $datas['Nilai'],
            ]);
        }


        return redirect('/result')->with('success', 'Data added successfully');
      
       
 
    }
    public function Scrape(Request $request)  
    {

        //all data
     

        
        //setting waktu eksekusi maksimal snscrape
        ini_set('max_execution_time', 0);
        //Eksekusi atau menjalankan script snscrape py
        //$output = shell_exec('python C:\xampp\htdocs\sna-app\app\Http\Controllers\testing.py "'.$request->katakunci1.'" "'.$request->katakunci2.'" "'.$request->katakunci3.'" "'.$request->katakunci4.'" "'.$request->startdate.'" "'.$request->enddate.'"');
        $output = shell_exec('python C:\xampp\htdocs\sna-app\app\Http\Controllers\testing.py');
        #echo($output);
        $var = json_decode($output, TRUE);
        
        $data=$var['Data'];
 
        unfilter::truncate();
        
             foreach($data as $datas) {
                unfilter::create([
                    'Tweet' => $datas['Tweet'],
                    'Username' => $datas['Username'],
                    'Followers' => $datas['Followers'],
                    'Following' => $datas['Following'],
                    'Reply' => $datas['Reply'],
                    'Date' => $datas['Date']
                ]);
            }
            return redirect('/')->with('success', 'Data added successfully');
    
    }




 


}
?>