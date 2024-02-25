<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

/**
 * @property int $donor_id // primary
 * @property int $recipient_id // primary
 * @property int $clinic_id
 * @property string $date
 * @property float $blood_amount // default 0
 *
// * @property-read Donor $donor
// * @property-read Recipient $recipient
// * @property-read Clinic $clinic
 */
class DonorRecipient extends Model
{
    protected $table = 'donors__recipient';

    public $timestamps = false;

    protected $fillable = [
        'donor_id',
        'recipient_id',
        'clinic_id',
        'date',
        'blood_amount',
    ];
}
