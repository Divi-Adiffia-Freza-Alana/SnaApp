<?php

use App\Http\Controllers\CrawlController;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

/*Route::get('/', function () {
    return view('welcome');
});*/
Route::get('/', function () {
    $articles = ['Article 1','Article 2','Article 3'];
    return view('home',['articles' => $articles]);
});

Route::get('/preprocess', function () {
    return view('preprocess' );
});


Route::get('/visualize',[CrawlController::class, 'visualize']);

Route::post('/scrape',[CrawlController::class, 'Scrape']);

Route::post('/setpreprocess',[PreprocessController::class, 'setpreprocess']);

Route::get('/sna',[CrawlController::class, 'Sna']);


