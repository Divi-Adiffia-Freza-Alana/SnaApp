<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;
use Illuminate\Support\Facades\Http;

class PreprocessController extends Controller
{
    public function setpreprocess(Request $request)
    {

        // dd($request->all());

        //exit();
        //dd($request->katakunci1);

        
        //Script snscrape
        //$command = 'snscrape twitter-search "'.$request->katakunci1.' OR '.$request->katakunci2.' OR '.$request->katakunci3.' OR '.$request->katakunci4.' lang:id since:'.$request->startdate.' until:'.$request->enddate.'"  > Mantap.json';
        //echo $command;
        //exit(); 
        //nama file yg di create
        $file_name = '\test.py';
        //route direktori file
        $realpath = 'C:\xampp\htdocs\sna-app\public'.$file_name;
 
       /* if (file_exists($realpath)) {
        //menghapus direktori file
        unlink($realpath);
        }*/
        //setting waktu eksekusi maksimal snscrape
        ini_set('max_execution_time', 0);
        
        //Eksekusi atau menjalankan script snscrape py
        $output = shell_exec($realpath);

        echo $output;

    }

    public function Crawl()
    {
          
        $response = Http::get('localhost:3000/unpreprocess')->json();
        dd($response);

    }









}
?>