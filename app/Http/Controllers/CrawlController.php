<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\unfilter;
use App\Models\sna;
use Illuminate\Support\Facades\DB;
use afrizalmy\BWI\BadWord;


class CrawlController extends Controller
{
    public function index()
    {
        //$datatable = unfilter::all();
   
       
        $datatable = DB::table('unfilter')->where('Followers', '>=', 2000 )->where('Reply','!=','null')->where('Badwords','!=','1')->get();
        $data = DB::table('unfilter')->get();
        return view('home',['datatablelist'=> $datatable,'datanotfilter'=>$data]);
       
 
    } 
    public function result()
    {
 
        //$datatable = unfilter::all();
       
        $datatable = DB::table('sna')->get();
        return view('result',['datatablelist'=> $datatable]);
       
 
    }

    public function badwords($words){

        $owned_urls = array('anjing', 'babi', 'eror', 'asw', 'ajg' ,'error', 'rusak', 'ogah', 'jelek', 'judi', 'gagal');
        foreach ($owned_urls as $url) {
            //if (strstr($string, $url)) { // mine version
            if (strpos($words, $url) !== FALSE) { // Yoshi version
                return true;
            }
        }
        return false;

    }
    public function sna()
    {

        //$datatable = unfilter::all();


       
        $datatable = DB::table('unfilter')->select('Username','Reply')->where('Followers', '>=', 2000 )->where('Reply','!=','null')->where('Badwords','!=','1')->get();
        //dd($datatable);
        $bit = base64_encode($datatable);
        //dd($bit);
        header('Content-Type: application/json; charset=utf-8');
        $bot = json_encode($bit,true);

        //setting waktu eksekusi maksimal snscrape
        ini_set('max_execution_time', 0); 
        //Eksekusi atau menjalankan script snscrape py
        $output = shell_exec('python C:\xampp\htdocs\sna-app\app\Http\Controllers\sna.py "'.$bot.'"');
        $var = json_decode($output, TRUE);
        $data=$var['Data'];
        //dd($data);

     

        sna::truncate();
        foreach($data as $datas) {
            sna::create([  
                'Username' => $datas['Username'],
                'Nilai' => $datas['Nilai'],
                'Dc' => $datas['Dc'],
                'Cc' => $datas['Cc'],
                'DcNormal' => $datas['DcNormal'],
                'CcNormal' => $datas['CcNormal'],
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
        $output = shell_exec('python C:\xampp\htdocs\sna-app\app\Http\Controllers\testing.py "'.$request->katakunci1.'" "'.$request->katakunci2.'" "'.$request->katakunci3.'" "'.$request->katakunci4.'" "'.$request->startdate.'" "'.$request->enddate.'"');
        //$output = shell_exec('python C:\xampp\htdocs\sna-app\app\Http\Controllers\testing.py');

        $var = json_decode($output, TRUE);
        $data=$var['Data'];
        //dd($data);
        unfilter::truncate();
        
             foreach($data as $datas) {
                unfilter::create([
                    'Tweet' => $datas['Tweet'],
                    'Username' => $datas['Username'],
                    'Followers' => $datas['Followers'],
                    'Following' => $datas['Following'],
                    'Reply' => $datas['Reply'],
                    'Date' => $datas['Date'],
                    'Like' => $datas['Like'],
                    'View' => $datas['View'],
                    'Badwords' => $this->badwords($datas['Tweet'])
            
                ]);
            }
            return redirect('/')->with('success', 'Data added successfully');
    
    }




 


}
?>