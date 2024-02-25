<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Collection;

/**
 * @property int $id
 *
 * @property int $blood_group_id
 * @property int|null $breed_id
 * @property string|null $breed
 * @property int $pet_type_id
 * @property int|null $avatar_id
 * @property string $name
 * @property int $age
 * @property float $weight
 * @property int $user_id
 *
// * @property-read Collection<Vaccination> $vaccinations
// * @property-read BloodGroup|null $bloodGroup
// * @property-read Breed $breedModel
// * @property-read PetType $petType
// * @property-read Avatar|null $avatar
// * @property-read User $user
 */
class Pet extends Model
{
    public $timestamps = false;

    protected $fillable = [
        'blood_group_id',
        'breed_id',
        'breed',
        'pet_type_id',
        'avatar_id',
        'name',
        'age',
        'weight',
        'user_id',
    ];
}
