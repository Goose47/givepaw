<?php

namespace App\Tables;

use App\Models\Pet;
use Okipa\LaravelTable\Abstracts\AbstractTableConfiguration;
use Okipa\LaravelTable\Table;
use Okipa\LaravelTable\Column;

class PetsTable extends AbstractTableConfiguration
{
    protected function table(): Table
    {
        return Table::make()->model(Pet::class);
    }

    protected function columns(): array
    {
        return [
            Column::make('id'),
            Column::make('blood_group_id'),
            Column::make('breed_id'),
            Column::make('breed'),
            Column::make('pet_type_id'),
            Column::make('avatar_id'),
            Column::make('name'),
            Column::make('age'),
            Column::make('weight'),
            Column::make('user_id'),
        ];
    }

    protected function results(): array
    {
        return [
            // The table results configuration.
            // As results are optional on tables, you may delete this method if you do not use it.
        ];
    }
}
