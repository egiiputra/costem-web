<script lang="ts">
	let files: FileList | undefined = $state();

	$inspect(files);

	function predicts() {
		fetch('localhost:8000/predicts', {
			method: 'POST',
			body: JSON.stringify({ username: 'example' }),
			headers: {
				'Content-Type': 'application/json'
			}
		});
	}
</script>

<form action="" onsubmit={predicts}>
	<input
		id="files"
		type="file"
		class="file:mr-4 file:rounded-full file:border-0 file:bg-violet-50 file:px-4 file:py-2 file:text-sm file:font-semibold file:text-violet-700 hover:file:bg-violet-100 dark:file:bg-violet-600 dark:file:text-violet-100 dark:hover:file:bg-violet-500"
		bind:files
		multiple
	/>
	<button
		class="mr-4 rounded-full border-0 bg-violet-50 px-4 py-2 text-sm font-semibold text-violet-700 hover:bg-violet-100 dark:bg-violet-600 dark:text-violet-100 dark:hover:bg-violet-500"
	>
		Try samples
	</button>

	<button
		class="mr-4 rounded-full border-0 bg-violet-50 px-4 py-2 text-sm font-semibold text-violet-700 hover:bg-violet-100 dark:bg-violet-600 dark:text-violet-100 dark:hover:bg-violet-500"
		onclick={predicts}
	>
		Predicts
	</button>
	<ul>
		{#each files as file}
			<li>
				<span>{file.name}</span>
			</li>
		{/each}
	</ul>
</form>
