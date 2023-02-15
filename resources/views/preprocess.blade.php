
@extends('mainlayout')
@section('title', 'Page Title')
@section('content')
<br><br>

<h2 style="text-align:center;">Preprocess Data</h2>

<form action="scrape" method="post">
    @csrf
    <div class ="row">
        <div class="col-md-6">
            <label for="exampleInputEmail1" class="form-label">Follower</label>
            <input type="text" class="form-control" id="follower" name="follower" required/>
        </div>
        <div class="col-md-6">
            <label for="exampleInputEmail1" class="form-label">Target Usernames</label>
            <select class="form-select" aria-label="Default select example">
                <option selected></option>
                <option value="true">True</option>
                <option value="false">False</option>
              </select>
        </div> 
    </div>

    <br>
    <button type="submit" class="btn btn-primary">Process</button>

  </form>

@endsection
