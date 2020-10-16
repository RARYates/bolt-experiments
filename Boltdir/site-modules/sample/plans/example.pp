plan sample::example(
  TargetSpec $targets,
) {

  $contents = run_task('sample::generate', $targets)
  run_task('sample::read', $targets, 'contents' => $contents.to_data)

}
