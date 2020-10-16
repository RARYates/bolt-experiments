plan stuff::rw(
  TargetSpec $nodes,
  String $file,
){
  $read = run_task('stuff::read', $nodes, file => $file)
  $write = run_task('stuff::write', localhost, data => $read.to_data)
  return $write
}
