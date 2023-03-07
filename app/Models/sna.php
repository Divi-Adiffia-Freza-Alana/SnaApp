<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class sna extends Model
{
    use HasFactory;
    protected $table = 'sna';
    protected $primaryKey = 'id';
    protected $fillable = ['Username', 'Nilai', 'Dc', 'Cc', 'DcNormal', 'CcNormal', 'updated_at', ' created_at' ];
}
