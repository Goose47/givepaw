@extends('base')
@section('table')
  <livewire:table :config="App\Tables\PetsTable::class"/>
@endsection