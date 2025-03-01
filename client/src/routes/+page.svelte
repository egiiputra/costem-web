<script lang="ts">
	import { Fileupload, Label, Helper } from 'flowbite-svelte';
	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell
	} from 'flowbite-svelte';

	interface Scores {
		sehat: number;
		giberella: number;
		anthracnose: number;
	}

	interface Data {
		filename: string;
		scores: Scores | undefined;
		output: string | undefined;
	}

	let files: FileList | undefined = $state();

	let results: Data[] = $derived.by(() => {
		if (files == undefined) return [];

		let res = [];

		for (const file of files) {
			res.push({
				filename: file.name,
				scores: undefined,
				output: undefined
			});
		}
		return res;
	});

	$inspect(files);
	$inspect(results);

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

<Label for="with_helper" class="pb-2">Upload file</Label>
<Fileupload id="with_helper" class="mb-2" accept="image/jpeg,image/png" bind:files multiple />
<Helper>PNG or JPG; MAX: 2MB</Helper>

<Table>
	<TableHead>
		<TableHeadCell>Product name</TableHeadCell>
		<TableHeadCell>Color</TableHeadCell>
		<TableHeadCell>Category</TableHeadCell>
		<TableHeadCell>Price</TableHeadCell>
	</TableHead>
	<TableBody tableBodyClass="divide-y">
		<TableBodyRow>
			<TableBodyCell>Apple MacBook Pro 17"</TableBodyCell>
			<TableBodyCell>Sliver</TableBodyCell>
			<TableBodyCell>Laptop</TableBodyCell>
			<TableBodyCell>$2999</TableBodyCell>
		</TableBodyRow>
		<TableBodyRow>
			<TableBodyCell>Microsoft Surface Pro</TableBodyCell>
			<TableBodyCell>White</TableBodyCell>
			<TableBodyCell>Laptop PC</TableBodyCell>
			<TableBodyCell>$1999</TableBodyCell>
		</TableBodyRow>
		<TableBodyRow>
			<TableBodyCell>Magic Mouse 2</TableBodyCell>
			<TableBodyCell>Black</TableBodyCell>
			<TableBodyCell>Accessories</TableBodyCell>
			<TableBodyCell>$99</TableBodyCell>
		</TableBodyRow>
	</TableBody>
</Table>
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
