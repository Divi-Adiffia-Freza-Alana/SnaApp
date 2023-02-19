
@extends('mainlayout')
@section('title', 'Page Title')
@section('content')
<br><br>

<h2 style="text-align:center;">Crawl Twitter Data</h2>

<form action="scrape" method="post">
    @csrf
    <div class ="row">
        <div class="col-md-6">
            <label for="exampleInputEmail1" class="form-label">Kata kunci 1</label>
            <input type="text" class="form-control" id="katakunci1" name="katakunci1" required/>
        </div>
        <div class="col-md-6">
              <label for="exampleInputEmail1" class="form-label">Kata kunci 2</label>
              <input type="text" class="form-control" id="katakunci2" name="katakunci2" required/>
        </div>
    </div>
    <br>
    <div class ="row">
        <div class="col-md-6">
              <label for="exampleInputEmail1" class="form-label">Kata kunci 3</label>
              <input type="text" class="form-control" id="katakunci3" name="katakunci3" required/>
        </div>
        <div class="col-md-6">
              <label for="exampleInputEmail1" class="form-label">Kata kunci 4</label>
              <input type="text" class="form-control" id="katakunci4" name="katakunci4" required/> 
        </div> 
    </div>
    <br>
    <div class="row">
        <div class="col-md-6">
            <label for="exampleInputEmail1" class="form-label">Start Date</label>
            <div class="input-group date" data-provide="datepicker">
                <input type="date" name="startdate" class="form-control">
                <div class="input-group-addon">
                    <span class="glyphicon glyphicon-th"></span>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <label for="exampleInputEmail1" class="form-label">End Date</label>
            <div class="input-group date" data-provide="datepicker">
                <input type="date" name="enddate" class="form-control">
                <div class="input-group-addon">
                    <span class="glyphicon glyphicon-th"></span>
                </div>
            </div>
        </div>
    </div>

    <br>
    <button type="submit" class="btn btn-primary">Scrape</button>

  </form>
  <br><br>
  <div class="row">
   
    <table id="example" name="example" class="table table-stripped mt-20 example">
        <thead>
            <tr>
                <th>No.</th>
                <th>Username</th>
                <th>Followers</th>
                <th>Following</th>
                <th>Username Target</th>
                <th>Date</th>  
            </tr>
        </thead>
       
        <tbody>
            @foreach($datatablelist as $data)
            <tr>
            <td>{{ $loop->iteration }}</td>
            <td>{{ $data->Username }}</td>
            <td>{{ $data->Followers }}</td>
            <td>{{ $data->Following }}</td>
            <td>{{ $data->Reply }}</td>
            <td>{{ $data->Date }}</td>
            </tr>
            @endforeach
        </tbody>
       
    </table>
</div>



@endsection
