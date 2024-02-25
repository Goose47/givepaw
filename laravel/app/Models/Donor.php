<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

/**
 * @property int $id
 * @property int $pet_id
 * @property int|null $recipient_id
 * @property int $city_id
 *
// * @property-read City
// * @property-read Pet
// * @property-read Recipient
 */
class Donor extends Model
{
    public $timestamps = false;

    protected $fillable = [
        'pet_id',
        'recipient_id',
        'city_id',
    ];
}
