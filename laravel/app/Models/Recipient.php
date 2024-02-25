<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

/**
 * @property int $id
 *
 * @property string $reason
 * @property int $blood_component_id
 * @property int $blood_amount
 * @property int $donor_amount
 * @property int $pet_id
 * @property int $clinic_id
 * @property string $end_actual_date
 *
// * @property-read Clinic $clinic
// * @property-read Pet $pet
// * @property-read BloodComponent $bloodComponent
 */
class Recipient extends Model
{
    public $timestamps = false;

    protected $fillable = [
        'reason',
        'blood_component_id',
        'blood_amount',
        'donor_amount',
        'pet_id',
        'clinic_id',
        'end_actual_date',
    ];
}
