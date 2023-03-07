<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class unfilter extends Model
{
    use HasFactory;
    protected $table = 'unfilter';
    protected $primaryKey = 'id';
    protected $fillable = ['Tweet', 'Username', 'Followers', 'Following', 'Reply', 'Date', 'Like', 'View', 'Badwords', 'updated_at', ' created_at' ];
}
