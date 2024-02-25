<?php

namespace App\Tables;

use App\Models\Pet;
use Okipa\LaravelTable\Abstracts\AbstractTableConfiguration;
use Okipa\LaravelTable\Table;

class PetsTable extends AbstractTableConfiguration
{
    protected function table(): Table
    {
        return Table::make()->model(Pet::class);
    }

    protected function columns(): array
    {
        return [
            // The table columns configuration.
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
