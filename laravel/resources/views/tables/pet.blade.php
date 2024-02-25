@extends('base')
@section('table')
  <livewire:table :config="App\Tables\UsersTable::class"/>
@endsection