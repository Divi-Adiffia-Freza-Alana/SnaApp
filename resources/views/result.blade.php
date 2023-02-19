
@extends('mainlayout')
@section('title', 'Page Title')
@section('content')
<br><br>

<h2 style="text-align:center;">Result Social Network Analysis</h2>


    <div class ="row">
       <div class="col-md-12">
        <img src="{{ URL::to('/') }}/path.png" alt="Graph" height="500" style=" display: block; margin-left: auto; margin-right: auto; width: auto;"> 
       </div>
    </div>
    <br><br>
  <div class="row">
   
    <table id="example" name="example" class="table table-stripped mt-20 example">
        <thead>
            <tr>
                <th>No.</th>
                <th>Username</th>
                <th>Nilai</th>
        </thead>
       
        <tbody>
            @foreach($datatablelist as $data)
            <tr>
            <td>{{ $loop->iteration }}</td>
            <td>{{ $data->Username }}</td>
            <td>{{ $data->Nilai }}</td>
            </tr>
            @endforeach

        </tbody>
       
    </table>
</div>



@endsection
