class CreateTracks < ActiveRecord::Migration[5.1]
  def change
    create_table :tracks do |t|
      t.string :name
      t.integer :core
      t.integer :alg
      t.integer :dse
      t.integer :ss
      t.integer :sf

      t.timestamps
    end
  end
end
